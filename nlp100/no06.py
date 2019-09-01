"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""


def n_gram(target, n):
    return {target[i:i + n] for i in range(len(target) - (n - 1))}


def bi_gram(target):
    return n_gram(target, 2)


x = bi_gram("paraparaparadise")
y = bi_gram("paragraph")
# 和集合
# xとyの要素のうち、重複を除いたもの
print(x.union(y))
# 積集合
# xとyの要素のうち、同一の値のみ
print(x.intersection(y))
# 差集合
# xとyの要素のうち、xにない要素のみ
print(x.difference(y))

# 「se」要素の存在チェック
print("se" in x.union(y))
