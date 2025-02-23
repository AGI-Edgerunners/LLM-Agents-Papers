#!/usr/bin/env python 
# encoding: utf-8 
# @author: yihuai lan
# @fileName: script_v4_step2.py 
# @date: 2024/3/3 14:36 
#
# describe:
#
# -*- coding: utf-8 -*-

import json
import os
import re
import time
import warnings

import requests
from hashlib import md5

PAPER_FOLDER = "papers"
PARSED_FOLDER = "parsed_v4"
CSS_FILE = "src/style.css"
CONFIG_FILE = "config.json"
USE_CSS = False

PARSED_DATA = []


def read_json(file: str) -> dict:
    f = open(file, 'r', encoding='utf-8')
    data = json.load(f)
    f.close()
    return data


def write_json(file: str, data: dict) -> None:
    f = open(file, 'w+', encoding='utf-8')
    json.dump(data, f, ensure_ascii=False, indent=4)


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
        temp_item = [f"[{i}](#{i.replace(' ','-').replace('&','')})" for i in item]
        readme_lines.append(f"* {', '.join(temp_item)}")
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
    readme_line = f"""- [{date}] **{title}** | {url_tag} | {code_tag}\n"""
    return readme_line


def parse_paper_block(block_title, block_datas) -> str:
    readme_lines = [f"### {block_title}"]
    block_datas = sorted(block_datas, key=lambda x: x.get('date', ''), reverse=True)
    for data in block_datas:
        readme_line = parse_paper_item(data)
        if readme_line:
            readme_lines.append(readme_line)
    readme_lines.append("---")

    if not os.path.exists(PARSED_FOLDER):
        os.mkdir(PARSED_FOLDER)
    return '\n'.join(readme_lines)


def read_parsed_by_category():
    files = os.listdir(PARSED_FOLDER)
    all_parsed_datas = {}
    for file_name in files:
        parsed_datas = read_json(f"{PARSED_FOLDER}/{file_name}")
        # all_parsed_datas.update(parsed_datas)
        for id_, data in parsed_datas.items():
            category = data.get('category', [])
            if not category:
                category = ['Others']
            for cate in category:
                if cate in all_parsed_datas:
                    all_parsed_datas[cate].append(data)
                else:
                    all_parsed_datas[cate] = [data]
    return all_parsed_datas


def parse_paper_section(category_sort: list) -> str:
    readme_lines = ["## :newspaper: Papers"]
    all_parsed = read_parsed_by_category()
    for cate in category_sort:
        readme_line = parse_paper_block(cate, all_parsed.get(cate, []))
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
