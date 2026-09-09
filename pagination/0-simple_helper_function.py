#!/usr/bin/env python3
""" Pagination """
def index_range(page, page_size):
    """ Pagination """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return ((start_index, end_index))
