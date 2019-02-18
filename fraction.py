def addFraction(num1,den1,num2,den2):
	den3 = den1 * den2
	num3 = (num1*den2) + (num2*den1)
	return (num3,den3)




# using tuples

def addFraction2(f1,f2):
	den3 = f1[1]*f2[1]
	num3 = (f[0]*f2[1]) + (f[1]*f2[0])
	return (num3,den3)

#using list

def addFraction2(f1,f2):
        den3 = f1[1]*f2[1]
        num3 = (f[0]*f2[1]) + (f[1]*f2[0])
        return [num3,den3]

#using dictionary

d = {}

def addFraction3(d1,d2):
	d["denominator"]=(d1["denominator"] * d2["denominator"])
	d["numerator"] = (d1["numerator"]*d2["denominator"]) + (d2["numerator"]*d1["denominator"])
	return d


