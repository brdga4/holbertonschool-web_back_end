#!/usr/bin/env python3
"""
Shebang for Task 9
"""


def insert_school(mongo_collection, **kwargs):
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
