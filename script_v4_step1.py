#!/usr/bin/env python 
# encoding: utf-8 
# @author: yihuai lan
# @fileName: script_v4_step1.py
# @date: 2024/3/1 11:18 
#
# describe:
#
import json
import os
import re
import warnings
from hashlib import md5

import requests

URL_FILE = "papers_v4.json"
PARSED_FOLDER = "parsed_v4"
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
    return {'title': title, 'authors': authors, 'date': date, 'pdf': pdf, 'abstract': abstract, 'code': '',
            'category': []}


def parse_paper():
    if os.path.exists(CONFIG_FILE):
        config = read_json(CONFIG_FILE)
    else:
        config = {}
    all_category = [cate.split('.')[0] for cate in config.get('Category_Sort',[])]
    files = os.listdir(PARSED_FOLDER)
    stored_datas = {}
    all_parsed_datas = {}
    for file_name in files:
        year = file_name.split('.')[0]
        parsed_datas = read_json(f"{PARSED_FOLDER}/{file_name}")
        stored_datas[year] = parsed_datas
        all_parsed_datas.update(parsed_datas)
    datas = read_json(URL_FILE)
    for data in datas:
        print(f"parse data: {json.dumps(data)}")
        url = data.get('url', '')
        code = data.get('code')
        md5_id = md5(url.encode()).hexdigest()
        parsed = {}
        if url:
            parsed = all_parsed_datas.get(md5_id, {})

        if not parsed and url.startswith('https://arxiv.org/abs/'):
            parsed = parse_by_crawl(url)
            if parsed and code:
                parsed['code'] = code
            if parsed:
                parsed['url'] = url
                category = parsed.get('category')
                if not category:
                    print('-'*20)
                    print(f"title: {parsed.get('title')}")
                    print(f"link: {url}")
                    category_str = '\n'.join([f'{idx}.{cate.split(".")[0]}' for idx,cate in enumerate(all_category)])
                    input_str = input(f"Please label the category of this paper: {category_str}\nInput the numbers with blank:")
                    category = [all_category[int(idx)] for idx in input_str.split(' ')]
                    parsed['category'] = category
                all_parsed_datas.update({md5_id: parsed})

                t = parsed.get('date')
                year = t.split('/')[0]

                if year in stored_datas:
                    stored_datas[year].update({md5_id: parsed})
                else:
                    stored_datas[year] = {md5_id: parsed}
    for year, datas in stored_datas.items():
        write_json(f'{PARSED_FOLDER}/{year}.json', datas)


if __name__ == '__main__':
    parse_paper()
