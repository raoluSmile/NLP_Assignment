#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Task: 形态还原算法,实现一个英语单词还原工具
    1) 输入一个单词;
    2) 如果词典里有该词，输出该词及其属性，转4)，否则，转3);
    3) 如果有该词的还原规则，并且，词典里有还原后的词，则输出还原后的词及其属性，转4，否则，调用<未登录词模块>;
    4) 如果输入中还有单词，转1)，否则，结束。
词典: http://nlp.nju.edu.cn/MT_Lecture/dic_ec.rar

License: Apache-2.0
Author: Qinglong Zhang, Lu Rao
E-mail: wofmanaf@gmail.com, raoluSmile@gmail.com
"""

from __future__ import absolute_import, division, print_function

from utils import read_dict
import time