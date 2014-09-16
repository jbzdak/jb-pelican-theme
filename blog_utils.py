# -*- coding: utf-8 -*-

import re
from jinja2.filters import do_striptags


def tagsort_by_popularity(tag_list):
    return sorted(tag_list, key=lambda x: len(x[1]), reverse=True)


def as_dict(arg, key=None):
    if key is None:
        return dict(arg)
    return dict([(getattr(o, key), o) for o in arg])


def truncate(text, arg, ellipsis='&hellip;'):
    matches = re.match('(\d+)([cw])', arg)
    text = do_striptags(text)
    if not matches:
        raise ValueError()
    count = int(matches.group(1))
    type = matches.group(2)

    if type == 'c':
        if count > len(text):
            return text
        else:
            return text[:count] + ellipsis
    elif type == 'w':
        arr = text.strip().split()
        if count > len(arr):
            return text
        else:
            return ' '.join(arr[:count]) + ellipsis