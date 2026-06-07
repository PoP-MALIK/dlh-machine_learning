#!/usr/bin/env python3
"""Python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by avg_score"""
    students = list(mongo_collection.find())
    for student in students:
        topics = student.get("topics",[])
        total = 0
        count = 0
        for topic in topics:
            total += topic.get("score", 0)
            count += 1
        if count == 0:
            average = 0
        else:
            average = total / count
        student["averageScore"] = average
    students.sort(key=lambda x: x["averageScore"], reverse=True)
    return students
