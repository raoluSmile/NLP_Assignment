#!/usr/bin/python3
# pip install spacy
# python -m spacy download en
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
import re

file_path = './data/assign/dic_ec.txt'

def read_dict(path):
    Dict = {}
    fd = open(path, 'r')
    for line in fd.readlines():
        tmp = []
        lineVec = str(line).strip().split('')
        for content in lineVec[1:-1]:
            # using regular expression to get the word attributes
            pattern = re.compile(r'([a-z]+).')
            if pattern.match(content):
                tmp.append(content)

        Dict[lineVec[0]] = tmp

    return Dict

def print_result(Dict, word):
    # print("original form: " + word)
    tmpStr = ''
    for inst in Dict[word]:
        tmpStr += (inst+' ')
    print("original form: {}\t\tpart of speech: {}".format(word, tmpStr))

def main(model=None):
    """Load pre-trained model, set up the pipeline"""
    if model is not None:
        nlp = spacy.load(model)
        # print("Loaded model %s" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        # print("Create blank 'en' model")

    Dict = read_dict(file_path)
    doc = input("Input a doc: ")

    for token in nlp(doc):
        Inputword = token
        lemma = token.lemma_
        print("Input word: ", Inputword, end='\t\t')
        if Inputword in Dict.keys():
            print_result(Dict, Inputword)
        elif lemma in Dict.keys():
            print_result(Dict, lemma)
        else:
            print("Transformation Failure......")
    print('------------------------------------')

if __name__ == '__main__':
    # main(model='en')
    while 1:
        main(model='en')


