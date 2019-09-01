"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(target):
    # return ''.join(map(lambda v: chr(219 - ord(v) if v.islower() else v), target))
    return ''.join(chr(219 - ord(v) if v.islower() else v) for v in target)
# アトバシュ暗号

text = "paraparaparadise"
ciphered = cipher(text)
print ciphered
ciphered = cipher(ciphered)
print cipher(ciphered)
