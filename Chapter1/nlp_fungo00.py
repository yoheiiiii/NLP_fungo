#00_文字列の逆順
#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
def upsidedown(s):
	str1 = s[::-1]
	return str1

upsidedown("stressed")