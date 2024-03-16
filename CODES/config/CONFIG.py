# ---encoding:utf-8---
# @Time    : 2024/3/16 18:51
# @Author  : stzz aiot tlzs
# @Email   ：stzzaiottlzs@gmail.com
# @Site    : aiot
# @File    : CONFIG.py
# @Project : milvus_project
# @Software: PyCharm
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(BASE_DIR)

import torch
from pathlib import Path


class Config(object):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    check_point = "bert-base-chinese"

    embedding_dim = 768

    datas_dir = Path(os.path.join(BASE_DIR, "CODES", "datas"))

    drission_page_init_file_path = datas_dir / "blog_spider_init"
