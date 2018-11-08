#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
License: Apache-2.0
Author: Qinglong Zhang, Lu Rao
E-mail: wofmanaf@gmail.com, raoluSmile@gmail.com
"""

from __future__ import absolute_import, division, print_function

import os


def read_dict(path):
    words_dict = []
    with open(path, 'r') as r:
        line = r.readlines()
        for i in line:
            word = i.split(',')
            words_dict.append(word[0])
    return words_dict


def convert_encoding(init_path, fmt):
    # init_path = "./data/assign/", fmt = ".txt"
    fin = [fname for fname in os.listdir(init_path) if fname[-4:] == fmt]
    for fname in fin:
        with open(init_path+fname, encoding='GB18030') as f:
            data = f.read()
        with open(init_path+fname, 'w', encoding='utf8') as f:
            f.write(data)