#!/usr/bin/env python3
"""Lists_all Python function"""
def list_all(mongo_collection):
    """Lists all documents in a collection."""
    documents = list(mongo_collection.find())
    if documents == []:
        return []
    return documents
