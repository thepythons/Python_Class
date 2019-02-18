# exercise1

hours=int(input("Enter Hours: "))
rate=int(input("Enter Rate: "))
if hours>40:
	pay=rate*40
	pay+=(hours-40)*1.5*rate
	print(pay)
else:
	pay=rate*hours
	print(pay)

# exercise 2
try:
	hours=int(input("Enter Hours: "))
	rate=int(input("Enter Rate: "))
	if hours>40:
       		pay=rate*40
        	pay+=(hours-40)*1.5*rate
        	print(pay)
	else:
        	pay=rate*hours
        	print(pay)
except:
	print("Please Enter A Numeric Value")

# exercise 3
try:
	score=float(input("Enter Score: "))
	if score<0.0 or score>1.0:
		print("Bad Score")
	else:
		if score>=0.9:
			print("A")
		elif score>=0.8:
			print("B")
		elif score>=0.7:
			print("C")
		elif score>=0.6:
			print("D")
		else:
			print("F")	
except:
	print("Bad Score")
