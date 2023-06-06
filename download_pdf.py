# -*- coding: utf-8 -*-
# @org: 辰风科技
# @author: lyh
# @fileName: download_pdf.py
# @date: 2023/6/6 23:40
#
# describe:
#
# @version 1.0 2023/6/6 23:40
import json
import os
import re
import warnings

import requests

PROXY = None


def read_json(file: str) -> dict:
    f = open(file, 'r', encoding='utf-8')
    json_data = json.load(f)
    f.close()
    return json_data


def pdf_downloader(url: str, pdf_file: str):
    try:
        res = requests.get(url, proxies=PROXY if PROXY else None)
    except Exception as e:
        warnings.warn(f"something wrong when visit the url {url} ERROR:{str(e)}")
        res = None
    if res is not None and res.status_code == 200:
        with open(pdf_file, 'wb+') as f:
            f.write(res.content)
            f.close()
    else:
        warnings.warn(f'the file {pdf_file}({url}) download failed')


Parsed_Folder = 'parsed'
PDF_Folder = 'PDF'
if not os.path.exists(Parsed_Folder):
    warnings.warn(f'the folder ./{Parsed_Folder}/ is not exist')
    exit(0)

if not os.path.exists(PDF_Folder):
    os.mkdir(PDF_Folder)

files = os.listdir(Parsed_Folder)
for file in files:
    datas: dict = read_json(os.path.join(Parsed_Folder, file))
    for id_, data in datas.items():
        pdf_link = data.get('pdf')
        title = data.get('title')
        if not pdf_link or not title:
            warnings.warn(f'pdf link or title not found from {data}')
            continue
        pattern = '.*(?=.json)'
        match = re.search(pattern, file)
        list_title = match.group() if match else 'Paper List'
        pdf_file = f'{PDF_Folder}/{list_title}/{title}.pdf'
        if not os.path.exists(f'{PDF_Folder}/{list_title}'):
            os.mkdir(f'{PDF_Folder}/{list_title}')

        pdf_file = pdf_file.replace(':', '：')
        if not os.path.exists(pdf_file):
            print(f'{pdf_link} downloading...')
            pdf_downloader(pdf_link, pdf_file)
            print(f'{pdf_link} save to {pdf_file}')
