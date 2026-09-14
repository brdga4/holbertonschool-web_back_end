#!/usr/bin/env python3
"""
Shebang for Task 11
"""

def schools_by_topic(mongo_collection, topic):
    """_summary_

    Args:
        mongo_collection (_type_): _description_
        topic (_type_): _description_

    Returns:
        _type_: _description_
    """
    return list(mongo_collection.find({ "topics": topic }))
