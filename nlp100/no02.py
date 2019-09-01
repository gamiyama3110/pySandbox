"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""


def print_kougo(value1, value2):
    length = len(value1)
    new_value = ""

    for i in range(length):
        new_value += value1[i] + value2[i]
    print(new_value)


print_kougo("パトカー", "タクシー")
