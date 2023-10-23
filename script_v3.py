# -*- coding: utf-8 -*-

import json
import os
import re
import time
import warnings

import requests
from hashlib import md5

PAPER_FOLDER = "papers"
PARSED_FOLDER = "parsed"
CSS_FILE = "src/style.css"
CONFIG_FILE = "config.json"
USE_CSS = False

HEADERS = {}
PROXY = None

PARSED_DATA = []


def read_json(file: str) -> dict:
    f = open(file, 'r', encoding='utf-8')
    data = json.load(f)
    f.close()
    return data


def write_json(file: str, data: dict) -> None:
    f = open(file, 'w+', encoding='utf-8')
    json.dump(data, f, ensure_ascii=False, indent=4)


def parse_cite(cite_str: str):
    pattern = '(?<=(?<!book)title={).*(?=})|(?<=(?<!book)title = {).*(?=})'
    match = re.search(pattern, cite_str)
    title = match.group() if match else ''

    pattern = '(?<=url={).*(?=})|(?<=url = {).*(?=})'
    match = re.search(pattern, cite_str)
    url = match.group() if match else ''

    pattern = '(?<=eprint={)\d{4}.\d{2}|(?<=eprint = {)\d{4}.\d{2}'
    match = re.search(pattern, cite_str)
    yy, mm, dd = (match.group()[:2], match.group()[2:4], match.group()[-2:]) if match else ('', '', '')
    if match:
        dd = '01' if dd == '00' else dd
        date = f'20{yy}/{mm}/{dd}'
    else:
        pattern = '(?<=year={).*(?=})|(?<=year = {).*(?=})'
        match = re.search(pattern, cite_str)
        year = match.group() if match else ''

        pattern = '(?<=month={).*(?=})|(?<=month = {).*(?=})'
        match = re.search(pattern, cite_str)
        mm = match.group() if match else ''
        date = f'{year}.{mm}' if mm else f'{year}'
    return {'title': title, 'url': url, 'date': date}


def parse_by_crawl(url: str):
    try:
        res = requests.get(url, proxies=PROXY if PROXY else None)
    except Exception as e:
        warnings.warn(f"something wrong when visit the url {url} ERROR:{str(e)}")
        res = None
    if res is not None and res.status_code == 200:
        html_text = res.content.decode()

        # title
        pattern = '(?<=<meta name="citation_title" content=").*?(?=" />)'
        match = re.search(pattern, html_text)
        title = match.group() if match else ''

        # authors
        pattern = '(?<=<meta name="citation_author" content=").*?(?=" />)'
        authors = re.findall(pattern, html_text)
        authors = [f"{author.split(', ')[1]} {author.split(', ')[0]}" if len(author.split(', ')) == 2 else author
                   for author in authors]

        # date
        pattern = '(?<=<meta name="citation_date" content=").*?(?=" />)'
        match = re.search(pattern, html_text)
        date = match.group() if match else ''

        # pdf
        pattern = '(?<=<meta name="citation_pdf_url" content=").*?(?=" />)'
        match = re.search(pattern, html_text)
        pdf = match.group() if match else ''

        # abs
        pattern = '(?<=<meta name="citation_abstract" content=").*?(?=" />)'
        match = re.search(pattern, html_text, re.S)
        abstract = match.group() if match else ''
    else:
        title = ''
        authors = []
        date = ''
        pdf = ''
        abstract = ''
        return {}
    return {'title': title, 'authors': authors, 'date': date, 'pdf': pdf, 'abstract': abstract}


def parse_recommendation_section(data: dict) -> str:
    readme_lines = ["## :yellow_heart: Recommendation", data.get('description', '')]
    for item in data.get('items', []):
        readme_lines.append(f"* [{item.get('name', '')}]({item.get('url', '')}): {item.get('description', '')}")
    return '\n'.join(readme_lines)


def parse_description_section(data: dict) -> str:
    now = time.localtime(time.time())
    readme_lines = ["## :writing_hand: Description",
                    data.get('date', '').format(f"{now.tm_year}/{now.tm_mon}/{now.tm_mday}\n"),
                    data.get('description', '')]
    for item in data.get('items', []):
        readme_lines.append(f"* {item}")
    return '\n'.join(readme_lines)


def parse_paper_item(data: dict) -> str:
    title = data.get('title')
    if not title:
        return ''
    date = data.get('date', '')
    url = data.get('url') if data.get('url') else data.get('url')
    code = data.get('code') if data.get('code') else data.get('code')
    if url:
        url_tag = f'[[paper]]({url})'
    else:
        url_tag = '[paper]'
    if code:
        code_tag = f'[[code]]({code})'
    else:
        code_tag = '[code]'
    readme_line = f"""\t- [{date}] **{title}** | {url_tag} | {code_tag}\n"""
    return readme_line


def parse_paper_block(file_name: str) -> str:
    print(f"parse file: {file_name}")
    pattern = '.*(?=.json)'
    match = re.search(pattern, file_name)
    block_title = match.group() if match else 'Paper List'
    datas = read_json(os.path.join(PAPER_FOLDER, file_name))
    if os.path.exists(f"{PARSED_FOLDER}/{file_name}"):
        stored_datas = read_json(f"{PARSED_FOLDER}/{file_name}")
    else:
        stored_datas = {}
    readme_lines = [f"- {block_title}"]
    block_datas = []
    for data in datas:
        print(f"parse data: {json.dumps(data)}")
        url = data.get('url', '')
        parsed = {}
        if url:
            parsed = stored_datas.get(md5(url.encode()).hexdigest(), {})
        if not parsed and isinstance(url, str) and url.startswith('https://arxiv.org/abs/'):
            parsed = parse_by_crawl(url)
            if parsed:
                stored_datas.update({md5(url.encode()).hexdigest(): parsed})
        if not parsed:
            parsed = parse_cite(data.get('cite', ''))
        data.update(parsed)
        block_datas.append(data)
    block_datas = sorted(block_datas, key=lambda x: x.get('date', ''), reverse=True)
    for data in block_datas:
        readme_line = parse_paper_item(data)
        if readme_line:
            readme_lines.append(readme_line)
    readme_lines.append("---")

    if not os.path.exists(PARSED_FOLDER):
        os.mkdir(PARSED_FOLDER)
    write_json(f"{PARSED_FOLDER}/{file_name}", stored_datas)

    return '\n'.join(readme_lines)


def parse_paper_section(category_sort: list) -> str:
    readme_lines = ["## :newspaper: Papers"]
    if not os.path.exists('papers'):
        return '\n'.join(readme_lines)
    else:
        files = os.listdir('papers')
        if not category_sort:
            files = sorted(files, reverse=True)
        else:
            files = category_sort
        for file in files:
            if file.endswith('.json'):
                readme_line = parse_paper_block(file)
                readme_lines.append(readme_line)
    return '\n'.join(readme_lines)


def init():
    if os.path.exists(CONFIG_FILE):
        config = read_json(CONFIG_FILE)
    else:
        config = {}
    title = config.get('Name', '')
    readme_sections = [
        f"# {title}",
        parse_description_section(config.get('Description')),
        parse_recommendation_section(config.get('Recommendation')),
        parse_paper_section(config.get('Category_Sort')),
        config.get('Star_History', '')
    ]
    md_text = '\n'.join(readme_sections)

    with open('README.md', 'w+', encoding='utf-8') as f:
        f.write(md_text)
        f.close()


if __name__ == '__main__':
    init()
