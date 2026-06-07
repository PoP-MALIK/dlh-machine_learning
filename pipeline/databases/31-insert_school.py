#!/usr/bin/env python3
"""Python function that inserts a new document in a collection"""
def insert_school(mongo_collection, **kwargs):
    """Inserts a new document and returns the new id"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
