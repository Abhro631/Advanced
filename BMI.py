Height=float(input("Enter height in centimeters: "))
Weight=float(input("Enter Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("Body Mass Index is {BMI}: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("Severely underweight")
	elif(BMI<=18.5):
		print("Underweight")
	elif(BMI<=25):
		print("Healthy")
	elif(BMI<=30):
		print("Overweight")
	else: print("Severely overweight")
else:("enter valid details")
#to calculate the body mass index of anyone
#easy to use just inpute desired values and know the condition of your body
#very useful for physical instructors
#coded by:Abhro Kumar Roy
