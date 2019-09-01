"""
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""
target = "stressed"
new_value = ""
# for v in target[::-1]:
for v in (reversed(target)):
    new_value += v
print(target + " -> " + new_value)
