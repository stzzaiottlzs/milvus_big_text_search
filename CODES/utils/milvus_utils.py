# ---encoding:utf-8---
# @Time    : 2024/3/17 05:24
# @Author  : stzz aiot tlzs
# @Email   ：stzzaiottlzs@gmail.com
# @Site    : aiot
# @File    : milvus_utils.py
# @Project : milvus_project
# @Software: PyCharm
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(BASE_DIR)

from pymilvus import (
    utility,
    connections,
    FieldSchema,
    DataType,
    CollectionSchema,
    Collection
)
from CODES.config.CONFIG import Config


def create_connection():
    connections.connect("default", host="ljxwtl.cn", port="19530")

def create_milvus_collection(milvus_collection_name):
    # 连接向量数据库
    connections.connect("default", host="ljxwtl.cn", port="19530")
    has_connection = utility.has_collection(milvus_collection_name)
    print("has_connection:", has_connection)
    fields = [
        FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
        FieldSchema(name="random", dtype=DataType.DOUBLE),
        FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=Config.embedding_dim)
    ]

    schema = CollectionSchema(fields, "big text milvus")
    print(f"Create collection {milvus_collection_name}")
    milvus_collection = Collection(milvus_collection_name, schema, consistency_level="Strong")
    print(utility.has_collection(milvus_collection_name))
    print(milvus_collection)


def __test_get_milvus_client__():
    milvus_collection_name = "milvus_big_text"
    create_milvus_collection(milvus_collection_name)


def insert_milvus_data(milvus_collection_name):
    milvus_collection = Collection(milvus_collection_name)
    print(milvus_collection)


def __test_insert_milvus_data__():
    milvus_collection_name = "milvus_big_text"
    create_connection()
    insert_milvus_data(milvus_collection_name)


if __name__ == '__main__':
    # __test_get_milvus_client__()
    __test_insert_milvus_data__()