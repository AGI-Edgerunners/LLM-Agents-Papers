# -*- coding: utf-8 -*-
# @author: lyh
# @fileName: script.py
# @date: 2023/4/8 2:55
#
# describe:
#
# @version 1.0 2023/4/8 2:55
import os
import json
import re
import warnings

PAPER_FOLDER = "papers"
CSS_FILE = "src/style.css"
CONFIG_FILE = "config.json"
USE_CSS = False


def read_json(file: str) -> dict:
    f = open(file, 'r', encoding='utf-8')
    data = json.load(f)
    f.close()
    return data


def read_css(file: str) -> str:
    f = open(file, 'r', encoding='utf-8')
    data = f.read()
    f.close()
    return data


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
        date = f'20{yy}.{mm}.{dd}'
    else:
        pattern = '(?<=year={).*(?=})|(?<=year = {).*(?=})'
        match = re.search(pattern, cite_str)
        year = match.group() if match else ''

        pattern = '(?<=month={).*(?=})|(?<=month = {).*(?=})'
        match = re.search(pattern, cite_str)
        mm = match.group() if match else ''
        date = f'{year}.{mm}' if mm else f'{year}'
    return {'title': title, 'url': url, 'date': date}


def init_with_css():
    css_text = """<style>
    *,
    *::before,
    *::after {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      font: normal 16px/1.5 "Helvetica Neue", sans-serif;
      background: #456990;
      color: #fff;
      overflow-x: hidden;
      padding-bottom: 50px;
    }  
    
    
    /* INTRO SECTION
    –––––––––––––––––––––––––––––––––––––––––––––––––– */
    
    .intro {
      background: #F45B69;
      padding: 100px 0;
    }
    
    .container {
      width: 90%;
      max-width: 1200px;
      margin: 0 auto;
      text-align: center;
    }
    
    h1 {
      font-size: 2.5rem;
    }
    
    
    /* TIMELINE
    –––––––––––––––––––––––––––––––––––––––––––––––––– */
    .timeline ul li {
      list-style-type: none;
      position: relative;
      width: 6px;
      margin: 0 auto;
      padding-top: 50px;
      background: #fff;
    }
    
    .timeline ul li::after {
      content: '';
      position: absolute;
      left: 50%;
      bottom: 0;
      transform: translateX(-50%);
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: inherit;
    }
    
    .timeline ul li div {
      position: relative;
      bottom: 0;
      width: 400px;
      padding: 15px;
      background: #F45B69;
    }
    
    .timeline ul li div::before {
      content: '';
      position: absolute;
      bottom: 7px;
      width: 0;
      height: 0;
      border-style: solid;
    }
    
    .timeline ul li:nth-child(odd) div {
      left: 45px;
    }
    
    .timeline ul li:nth-child(odd) div::before {
      left: -15px;
      border-width: 8px 16px 8px 0;
      border-color: transparent #F45B69 transparent transparent;
    }
    
    .timeline ul li:nth-child(even) div {
      left: -439px;
    }
    
    .timeline ul li:nth-child(even) div::before {
      right: -15px;
      border-width: 8px 0 8px 16px;
      border-color: transparent transparent transparent #F45B69;
    }
    </style>
    """
    if os.path.exists(CSS_FILE):
        css = read_css(CSS_FILE)
        css_text = f"""<style>
        {css}
        </style>
        """
    else:
        warnings.warn("can not find css file: {}".format(CSS_FILE))
        css = ''
    if os.path.exists(CONFIG_FILE):
        config = read_json(CONFIG_FILE)
    else:
        config = {}

    title = config.get('repo')
    description = config.get('description')

    line_head = f"""
    <section class="intro">
      <div class="container">
        <h1>{title}</h1>
        {description}
      </div>
    </section>
    """
    line_body = []
    if not os.path.exists('papers'):
        pass
    else:
        files = os.listdir('papers')
        files = sorted(files, reverse=True)
        for file in files:
            if file.endswith('.json'):
                datas = read_json(os.path.join(PAPER_FOLDER, file))
                for data in datas:
                    parsed = parse_cite(data.get('cite', ''))
                    title = parsed.get('title')
                    if not title:
                        warnings.warn("can not parse data: {}".format(data))
                        continue
                    year = parsed.get('year', '')
                    url = parsed.get('url') if parsed.get('url') else data.get('url')
                    code = data.get('code')
                    if url:
                        url_tag = f'<a href="{url}">[paper]</a>'
                    else:
                        url_tag = '<p>[paper]</p>'
                    if code:
                        code_tag = f'<a href="{code}">[code]</a>'
                    else:
                        code_tag = '[code]'
                    item = f"""<li><div><time>[{year}]</time> {title} | {url_tag} | {code_tag}</div></li>"""
                    line_body.append(item)

            else:
                continue
    line_body_str = '\n'.join(line_body)
    line_body_str = f"""
    <section class="timeline">
      <ul>
      {line_body_str}
      </ul>
    </section>
    """
    time_line = f"""
    {line_head}
    
    {line_body_str}
    """

    md_text = f"""
    {css_text}
    
    {time_line}
    """

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(md_text)
        f.close()


def init():
    if os.path.exists(CONFIG_FILE):
        config = read_json(CONFIG_FILE)
    else:
        config = {}

    title = config.get('repo')
    description = config.get('description')
    all_list = []
    line_head = f"""# {title}\n{description}\n\n---"""
    if not os.path.exists('papers'):
        pass
    else:
        files = os.listdir('papers')
        files = sorted(files, reverse=True)
        for file in files:
            pattern = '.*(?=.json)'
            match = re.search(pattern, file)
            list_title = match.group() if match else 'Paper List'
            list_block = []
            if file.endswith('.json'):
                datas = read_json(os.path.join(PAPER_FOLDER, file))
                parsed_datas = []
                for data in datas:
                    parsed = parse_cite(data.get('cite', ''))
                    title = parsed.get('title')
                    if not title:
                        warnings.warn("can not parse data: {}".format(data))
                        continue
                    year = parsed.get('date', '')
                    url = data.get('url') if data.get('url') else parsed.get('url')
                    code = data.get('code')
                    if url:
                        url_tag = f'[[paper]]({url})'
                    else:
                        url_tag = '[paper]'
                    if code:
                        code_tag = f'[[code]]({code})'
                    else:
                        code_tag = '[code]'
                    parsed_datas.append({'year': year, 'title': title, 'url': url_tag, 'code': code_tag})
                parsed_datas = sorted(parsed_datas, key=lambda x: x.get('year', ''), reverse=True)
                for data in parsed_datas:
                    year = data.get('year')
                    title = data.get('title')
                    url_tag = data.get('url')
                    code_tag = data.get('code')
                    item = f"""\t- [{year}] *{title}* | {url_tag} | {code_tag}\n"""
                    list_block.append(item)

            else:
                continue
            block_str = '\n'.join(list_block)
            all_list.append(f"""- {list_title}\n{block_str}""")
    line_body = "\n---\n".join(all_list)
    time_line = f"""{line_head}\n\n{line_body}"""

    md_text = f"""{time_line}"""

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(md_text)
        f.close()


if __name__ == '__main__':
    init()
