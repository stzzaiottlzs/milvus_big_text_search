# ---encoding:utf-8---
# @Time    : 2024/3/16 17:04
# @Author  : stzz aiot tlzs
# @Email   ：stzzaiottlzs@gmail.com
# @Site    : aiot
# @File    : predict.py
# @Project : milvus_project
# @Software: PyCharm
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(BASE_DIR)

from transformers import AutoTokenizer, AutoModel
from CODES.config.CONFIG import Config

tokenizer = AutoTokenizer.from_pretrained(Config.check_point, mirror="tuna")
model = AutoModel.from_pretrained(Config.check_point, mirror="tuna")

inputs = tokenizer("你好，中国", padding=False, return_tensors="pt")

print(inputs)

embeddings = model.embeddings(inputs["input_ids"])

print(embeddings.shape)
