# project structure
```text
Runners-On-XXXX
    |----papers
          |----2023.json
          |----2022.json
          |···
    |----script.py  
```

# Usage
1. Write `config.json` file including your repo name and the description of it.

2. The folder `papers` saves all papers you collected, and these papers classified by year(or other rules).

3. Run ```python script_v2.py``` to generate README.md automatically.

# Format of writing the information of a paper to json file
```json
[
  {
    "cite": "BibTeX Citation String copied here",
    "url": "paper link copied here",
    "code": "code address copied here"
  },
  {
    "cite": "misc{wu2023visual,\n      title={Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models}, \n      author={Chenfei Wu and Shengming Yin and Weizhen Qi and Xiaodong Wang and Zecheng Tang and Nan Duan},\n      year={2023},\n      eprint={2303.04671},\n      archivePrefix={arXiv},\n      primaryClass={cs.CV}\n}",
    "url": "https://arxiv.org/abs/2303.04671",
    "code": "https://github.com/microsoft/visual-chatgpt"
  }
]
```

# Attention
If you clone this repo and then build your paper list repo, remember to delete .git/* and reinitialize it before pushing.
