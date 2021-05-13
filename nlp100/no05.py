#!/usr/bin/env python3
"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def n_gram(target, n):
    return [target[i: i + n] for i in range(len(target) - (n - 1))]
# for文を1行でまとめる方法
# https://www.yoheim.net/blog.php?q=20150702


text = "I am an NLPer"
print(n_gram(text, 2))
print(n_gram(text.split(), 2))
