#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Task: 实现一个基于词典与规则的汉语自动分词系统.
词典: http://nlp.nju.edu.cn/MT_Lecture/dic_ce.rar

License: Apache-2.0
Author: Qinglong Zhang, Lu Rao
E-mail: wofmanaf@gmail.com, raoluSmile@gmail.com
"""

from __future__ import absolute_import, division, print_function

from utils import read_dict
import time


class MaxSegmentation(object):
    """
    Args:
        words_dict: list 字典
        sentence: str 待划分句子
        max_len: int 最大词长 默认为4
    Return:
        word_list: list 分词后的单词列表
    """
    def __init__(self, words_dict, sentence='', max_len=4):
        self.max_len = max_len
        self.sentence = sentence
        self.words_dict = words_dict

    def ForwardMM(self):
        """
        正向最大匹配算法（MM）：按照人得而自然阅读顺序从左往右对一段话甚至文章进行词库匹配切分。
        算法描述：
            设MaxLen为最大词长,D为分词词典
            （1）从待切分语料中按正向取长度为MaxLen的字符串str，令Len =MaxLen；
            （2）将str与D中的词语互相匹配；
            （3）if匹配成功，将指针向前移Len个汉字，并返回到（1）；
            （4）if 不成功：
            　　　　if（ Len>1）：
            　　　　　　Len = Len-1；
            　　　　　　从待切分语料中取长度为Len的字符串str，并返回（2）；
            　　　　else：
            　　　　　　得到单个汉字，指针向前移一个汉字，并返回（1）
        """
        sen_len = self.sentence.__len__()  # 原句长度
        index = 0   # 表示分词的位置
        word_list = []  # 划分的结果
        while index < sen_len:
            l = None
            for l in range(self.max_len, 0, -1):
                if self.sentence[index: index+l] in self.words_dict:
                    break
            word_list.append(self.sentence[index: index+l])
            index += l
        return word_list


    def ReverseMM(self):
        """
        逆向最大匹配算法（RMM）：主要原理与正向最大匹配算法一致，只是切分方向相反，从文章的尾部开始匹配。
        """
        sen_len = self.sentence.__len__()  # 原句长度
        index = sen_len  # 表示分词的位置
        word_list = []  # 划分的结果

        while index > 0:
            l = None
            if self.max_len > index:
                self.max_len = index
            for l in range(self.max_len, 0, -1):
                if self.sentence[index-l: index] in self.words_dict:
                    break
            word_list.insert(0, self.sentence[index-l: index])
            index -= l
        return word_list
    
    def BMM(self):
        """
        双向最大匹配法是将正向最大匹配法得到的分词结果和逆向最大匹配法的到的结果进行比较，从而决定正确的分词方法。
        启发式规则：
            1.如果正反向分词结果词数不同，则取分词数量较少的那个。
            2.如果分词结果词数相同
                a.分词结果相同，就说明没有歧义，可返回任意一个。
                b.分词结果不同，返回其中单字较少的那个。
        """
        forward = self.ForwardMM()
        reverse = self.ReverseMM()
        total_fmm, total_rmm = len(forward), len(reverse)   # 总词数
        if total_fmm != total_rmm:
            return forward if total_fmm < total_rmm else reverse
        else:
            if forward == reverse:
                return forward
            else:
                f_single_word, r_single_word = self.count_single_words(forward, reverse)    # 单字词数
                return forward if f_single_word < r_single_word else reverse

    def count_single_words(self, word_list):
        """
        统计单字词的个数
        Args:
            words_list: list 单词列表
        Return:
            count: int 单字词个数
        """
        count = 0
        for word in word_list:
            if len(word) == 1:
                count += 1
        return count


if __name__ == '__main__':

    words_dict = read_dict('./data/assign/dic_ce.txt')
    max_len = len(max(words_dict, key=len))
    test = "我正在上自然语言处理课。"
    segment = MaxSegmentation(words_dict, test, max_len)
    fstart = time.time()
    f_result = segment.ForwardMM()
    fend = time.time()
    print("ForwardMM： {}, running time: {} s".format(f_result, str(fend-fstart)))
    rstart = time.time()
    r_result = segment.ReverseMM()
    rend = time.time()
    print("ReverseMM： {}, running time: {} s".format(r_result, str(rend-rstart)))
    bistart = time.time()
    bi_result = segment.BMM()
    biend = time.time()
    print("BMM： {}, running time: {} s".format(f_result, str(biend-bistart)))

