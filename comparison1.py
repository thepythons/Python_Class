# comparison using if with boolean conditional expression

def maximum(a,b,c):
	if a>b and a>c:
		return a
	elif b>a and b>c:
		return b
	else:
		return c

# comparison using nested if

def maximum2(a,b,c):
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

# comparison using if expression
def maximum3(a,b,c):
	 return a if a>b and a>c else b if b>c and b>a else c 

		
