#!/usr/bin/python3
# pip install spacy
# python -m spacy download en_core_web_sm
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


import spacy

file_path = './data/assign/dic_ec.txt'

def read_dict(path):
    Dict = {}
    fd = open(path, 'r')
    for line in fd.readlines():
        tmp = []
        lineVec = str(line).strip().split('')
        for content in lineVec[1:-1]:
            if '.' in str(content):
                tmp.append(content)
        Dict[lineVec[0]] = tmp

    return Dict

def print_result(Dict, word):
    print("original form: " + word)
    tmpStr = ''
    for inst in Dict[word]:
        tmpStr += (inst+'\t')
    print("part of speech: " + tmpStr)


def main():
    Dict = read_dict(file_path)
    doc = input("Input an English word: ")

    nlp = spacy.load('en_core_web_sm')
    for token in nlp(doc):
        Inputword = token
        lemma = token.lemma_

    if Inputword in Dict.keys():
        print_result(Dict, Inputword)
    elif lemma in Dict.keys():
        print_result(Dict, lemma)
    else:
        print("Transformation Failure......")

if __name__ == '__main__':
    while 1:
        main()