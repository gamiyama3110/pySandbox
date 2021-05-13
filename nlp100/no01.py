#!/usr/bin/env python3
"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""
target = "パタトクカシーー"
for i in range(len(target)):
    if i % 2 == 0:
        continue
    print(target[i], end="")
