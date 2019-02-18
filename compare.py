# using if with boolean conditions

def compare(a,b,c):
	if a>b and b>c:
		return a
	elif b>a and a>c:
		return b
	else:
		return c


# using if expression

def compare(a,b,c):
	return a if a>b and a>c else b if b>a and b>c else c


#using nested if

def compare(a,b,c):
	if a>b:
		if b>c:
			return a
		elif c>a:
			return c

	elif b>c:
		if c>a:
			return b
		elif c>b:
			return c
	elif c>a:
		if a>b:
			return c
		elif b>c:
			return b
