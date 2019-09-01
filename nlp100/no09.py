"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
その実行結果を確認せよ．
"""
import random


def transpose_words(target):
    res = []
    for word in target.split():
        if len(word) > 4:
            shuffle_arr = list(word)[1:-1]
            random.shuffle(shuffle_arr)
            word = word[0] + ''.join(shuffle_arr) + word[-1]
        res.append(word)
    return ' '.join(res)


text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(transpose_words(text))
