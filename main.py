rate=input("Please Enter Hour Rate Salary:")
r=float(rate)
daily=(r*8)
weekly=(r*5*8)
monthly=(r*22*8)
yearly=(r*264*8)

print("D = Daily Salary")
print("W = Weekly Salary")
print("M = Monthly Salary")
print("Y = Yearly Salary")
time=input("Please Enter What you want to Calculate:")
print("Your Selection is:"+time)

if(time)=="D":
 print("The Daily Salary is:",daily,"OMR")
elif(time)=="W":
	print("The Weekly Salary is:",weekly,"OMR")
elif(time)=="M":
	print("The Monthly Salary is:",monthly,"OMR")
elif (time)=="Y":
	print("The Yearly Salary is:",yearly,"OMR")
else:
	print("Your Input is Invailid, Retry!!!")

	#python comments