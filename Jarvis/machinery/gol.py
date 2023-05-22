# -*- coding: utf-8 -*-


def _init():
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    _global_dict[key] = value


def get_value(key, defValue=0):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue


def add_value(key):
    if key not in _global_dict:
        _global_dict[key] = 1
    else:
        _global_dict[key] = _global_dict[key] + 1


def transfer():
    print(_global_dict)
