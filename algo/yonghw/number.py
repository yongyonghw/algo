import re
def hide_number(s):
	start = s[0:len(s)-4]
	start2 = re.sub('[0-9]', '*',  start)
	end = s[len(s)-4:len(s)]
	return start2 + end;
print(hide_number('01033334444'));



