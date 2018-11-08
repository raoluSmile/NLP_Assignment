#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from __future__ import absolute_import, division, print_function

from utils import read_dict
import time

class MM(object):
    def __init__(self, window_size, source, words_dict):
        self.window_size = window_size
        self.source = source
        self.words_dict = words_dict

    # 正向匹配算法
    def fmm(self):
        len_source = len(self.source)  # 原句长度
        index = 0
        words = []  # 分词后句子每个词的列表

        while index < len_source:  # 如果下标未超过句子长度
            match = False
            for i in range(self.window_size, 0, -1):
                sub_str = self.source[index: index+i]
                if sub_str in words_dict:
                    match = True
                    words.append(sub_str)
                    index += i
                    break
            if not match:
                words.append(self.source[index])
                index += 1
        return words


    # 反向匹配算法
    def rmm(self):
        len_source = len(self.source)  # 原句长度
        index = len_source
        words = []  # 分词后句子每个词的列表

        while index > 0:
            match = False
            for i in range(self.window_size, 0, -1):
                sub_str = self.source[index-i: index]
                if sub_str in words_dict:
                    match = True
                    words.append(sub_str)
                    index -= i
                    break
            if not match:
                words.append(self.source[index-1])
                index -= 1
        words.reverse()  # 得到的列表倒序
        return words

    # 双向匹配算法
    def bi_mm(self):
        forward = self.fmm()
        backward = self.rmm()
        # 正反向分词结果
        # print("FMM: ", forward)
        # print("RMM: ", backward)
        # 单字词个数
        f_single_word = 0
        b_single_word = 0
        # 总词数
        tot_fmm = len(forward)
        tot_rmm = len(backward)
        # 非字典词数
        oov_fmm = 0
        oov_rmm = 0
        # 罚分，罚分值越低越好
        score_fmm = 0
        score_rmm = 0
        # 如果正向和反向结果一样，返回任意一个
        if forward == backward:
            return backward
        # print(backward)
        else:  # 分词结果不同，返回单字数、非字典词、总词数少的那一个
            for each in forward:
                if len(each) == 1:
                    f_single_word += 1
            for each in backward:
                if len(each) == 1:
                    b_single_word += 1
            for each in forward:
                if each not in words_dict:
                    oov_fmm += 1
            for each in backward:
                if each not in backward:
                    oov_rmm += 1
            # 可以根据实际情况调整惩罚分值
            # 这里都罚分都为1分
            # 非字典词越少越好
            if oov_fmm > oov_rmm:
                score_rmm += 1
            elif oov_fmm < oov_rmm:
                score_fmm += 1
            # 总词数越少越好
            if tot_fmm > tot_rmm:
                score_rmm += 1
            elif tot_fmm < tot_rmm:
                score_fmm += 1
            # 单字词越少越好
            if f_single_word > b_single_word:
                score_rmm += 1
            elif f_single_word < b_single_word:
                score_fmm += 1

            # 返回罚分少的那个
            if score_fmm < score_rmm:
                return forward
            else:
                return backward


if __name__ == '__main__':

    words_dict = read_dict('./data/assign/dic_ce.txt')
    window_size = len(max(words_dict, key=len))
    test = "我正在上自然语言处理课。"
    segment = MM(window_size, test, words_dict)
    fstart = time.time()
    f_result = segment.fmm()
    fend = time.time()
    print("FMM： {}, running time: {} s".format(f_result, str(fend-fstart)))
    rstart = time.time()
    r_result = segment.rmm()
    rend = time.time()
    print("RMM： {}, running time: {} s".format(f_result, str(rend-rstart)))
    bistart = time.time()
    bi_result = segment.bi_mm()
    biend = time.time()
    print("BiMM： {}, running time: {} s".format(f_result, str(biend-bistart)))

