name = input("Enter your name: ")
student = input("Are you a student of DLL? (yes/no) : ")

if student.lower() == "yes" :
		yearLevel = input("What year level are you? \nF - Freshmen \nJ- Junior \nS - Sophomore \nR - Senior \nYour answer: ")
		if yearLevel.lower() == "f" :
			print(f" Hi, {name} freshmen, Welcome to DLL")


		elif yearLevel.lower() == "j" :
			print(f" Hi, {name} junior, Welcome to DLL")

		elif yearLevel.lower() == "s" :
			print(f" Hi, {name} sophomore, Welcome to DLL")

		elif yearLevel.lower() == "r" :
			print(f" Hi, {name} senior, Welcome to DLL")

else :
		print("Thank you for using the system")
	
 