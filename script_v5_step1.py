#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project: LLM-Agents-Papers
File: script_v5_step1.py
Date: 2025/2/23 02:00
"""
import json
import os
import warnings
import re
from hashlib import md5

import requests

URL_FILE = "papers_v5.json"
PARSED_FOLDER = "parsed_v5"
CSS_FILE = "src/style.css"
CONFIG_FILE = "config_v5.json"
USE_CSS = False

HEADERS = {}
PROXY = None #{"https": "127.0.0.1:4780", "http": "127.0.0.1:4780"}

PARSED_DATA = []

stored_datas = {}
all_parsed_datas = {}

def read_json(file: str) -> dict:
    f = open(file, 'r', encoding='utf-8')
    data = json.load(f)
    f.close()
    return data


def write_json(file: str, data: dict) -> None:
    f = open(file, 'w+', encoding='utf-8')
    json.dump(data, f, ensure_ascii=False, indent=4)
    f.close()

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

def pretty_category(all_categories):
    columns = 2
    max_len = max(len(cate.split(".")[0]) for cate in all_categories)
    rows = (len(all_categories) + 1) // columns

    lines = []
    for i in range(rows):
        left = f'{i}.{all_categories[i].split(".")[0]}'.ljust(max_len + 4)
        right_idx = i + rows
        right = f'{right_idx}.{all_categories[right_idx].split(".")[0]}' if right_idx < len(all_categories) else ''
        lines.append(left + right)

    # print('\n'.join(lines))
    return '\n'.join(lines)


def parse_paper():
    global stored_datas, all_parsed_datas
    if os.path.exists(CONFIG_FILE):
        config = read_json(CONFIG_FILE)
    else:
        config = {}
    # all_category = [cate.split('.')[0] for cate in config.get('Category_Sort',[])]
    all_categories = []
    category_mapping = {}
    cat_idx = 0
    for category_1, sub_categories in config.get("Description",{}).get("items", {}).items():
        if not sub_categories:
            all_categories.append(category_1)
            category_mapping[cat_idx] = [category_1, None]
            cat_idx += 1
        else:
            for sub_category in sub_categories:
                all_categories.append(sub_category)
                category_mapping[cat_idx] = [category_1, sub_category]
                cat_idx += 1

    files = os.listdir(PARSED_FOLDER)
    for file_name in files:
        year = file_name.split('.')[0]
        parsed_datas = read_json(f"{PARSED_FOLDER}/{file_name}")
        stored_datas[year] = parsed_datas
        all_parsed_datas.update(parsed_datas)
    datas = read_json(URL_FILE)
    for data_idx,data in enumerate(datas):
        print(f"parse data: {json.dumps(data)}")
        print("{}/{}".format(data_idx+1, len(datas)))
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
                    print(f"title: {parsed.get('title')}  link: {url}")
                    # print(f"link: {url}")
                    # category_str = '\n'.join([f'{idx}.{cate.split(".")[0]}' for idx,cate in enumerate(all_categories)])
                    # for idx in range(len(all_categories)):
                    #     if idx%2==1:
                    #         category_str = category_str.replace(f"\n{idx}",f" {idx}",1)
                    category_str = pretty_category(all_categories)
                    input_str = input(f"Please label the category of this paper: \n{category_str}\nInput the numbers with blank:")
                    category = [category_mapping[int(idx)] for idx in input_str.split(' ')]
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
    try:
        parse_paper()
    except Exception as e:
        for year, datas in stored_datas.items():
            write_json(f'{PARSED_FOLDER}/{year}.json', datas)
