def act22():
      print("=" * 161)
      print("WELCOME TO THE PROGRAM".center(150))
      print("=" * 161)

      print("=" * 161)
      name = input("Enter your name: ").strip()
      print(f"Hello, {name}! Welcome to the program!")
      print("=" * 161)

      print("=" * 161)
      print("THIS PROGRAM IS FOR FINAL PROJECT OF VINCENT FROM BSIT-1A")
      print("TO ENTER TO THE PROGRAM PLEASE ENTER THE PASSWORD")
      print("=" * 161)

                  
      def act1():
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\b\t*\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b* * *",
            "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b* * * * *\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b\b\b* * * * * * *",
            "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b* * * * *\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b* * *",
            "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t*\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b")

      def act2():
            name= input("please enter your name:")
            print("Hi" + name)
      def act3():
            fullname = input("please input your full name:")

            City = input("please input your city:")

            Province = input("please input your province:")

            Postal_code = input("please input the postal code of the province:")

            Cellphonenumber = input("please input your cellphone number:")

            Email = input("please input your email:")

            Birthday = input("please input you birhday:")

            BirthPlace = input("please input your birth place:")

            Age = input("please input your age:")

            CivilStatus = input("please input your civil status:")

            Height = input("please input your height in ft:")

            Weight = input("please input your weight in kg:")

            Religion = input("please input your religion:")

            Gender = input("please input your gender:")

            Citezenship = input("please input your cintezenship:")

            FatherName = input("please input your father's name:")

            SiblingName = input("please input your sibling's name:")

            print("My name is:" + fullname + 
            "\nI'm from the city of:" + City + 
            "\nI'm from the province of:" + Province + 
            "\nThe postal code of:" + Province + ",is the:" + Postal_code + 
            "\nMy cellphone number is:" + Cellphonenumber + 
            "\nMy Email is:" + Email + 
            "\nMy Birthday is:" + Birthday + 
            "\nMy Birth Place:" + BirthPlace + 
            "\nMy age is:" + Age + 
            "\nMy civil status is:" + CivilStatus +
            "\nMy height in Ft is:" + Height + 
            "\nMy weight in kilogram is:" + Weight + 
            "\nMy religion is:" + Religion + 
            "\nMy gender:" +Gender + 
            "\nMy citezenship is" + Citezenship + 
            "\nMy Father's full name is:" + FatherName + 
            "\nMy sibling's full name is:" + SiblingName + 
            "\nThis is my BIONOTE") 

      def act4():
            number1= int(input("enter a number :"))
            number2= int(input("enter a number :"))
            answer= number1 + number2
            print(f"The sum of {number1} + {number2} is {answer}")

      def act5():
            print("FARENHEIT TO CELSIUS CONVERTER PROGRAM")
            farenheit= eval(input("enter temperature in farenheit:"))
            celsius= ((farenheit-32)* 5 )/9
            print(f"{farenheit}, degrees Farenheit converted to celsius is {round(celsius,2)} degrees")

      def act6():
            x = 5
            print(x)    

            x += 10
            print(x)

            x += 15
            print(x)

            x+= 10
            print(x)

      def act7():
            gold=0
            miner= input("Hi, what is ypour name:")
            isgold= input("is the mineral gold?")

            if isgold == "yes":
                  gold+=1 
                  print(f" Hi {miner}, Your total number of gold is {gold}")
            else:
                  print(f"INVALID")

      def act8():
            password= input("enter your password: ")

            if password. lower() == "secret":
                  print(" Access Granted")
                  print(" Enjoy using the System")

            elif password. lower() == "maspogikaysir12":

                  print(" Enjoy using the System")

            else:
                  print(" access denied")

      def act9():
            age = int(input("Enter your Age: "))

            if age > 130:
                  print("Enter your Real Age")
            elif age >= 60 and age <= 130:
                  print("You are a senior")
            elif age >= 46 and age <= 59:
                  print("You are at Post Adulthood")
            elif age >= 32 and age <= 45:
                  print("You are at Mid Adulthood")
            elif age >= 19 and age <= 31:
                  print("You are at an Early Adulthood")
            elif age >= 14 and age <= 18:
                  print("You are a Teenager")
            elif age >= 8 and age <= 13:
                  print("You are at Pre-Teen")
            elif age >= 1 and age <= 7:
                  print("You are a Todler")
            else:
                  print("Enter a your Real Age")

      def act10():
            
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
                              

      def act11():
            for i in range(1, 11):
                  print("Hello World!")
                  print("Happy world")
                  
                  single = False

                  print(f"{single}, That I'm Single")

      def act12():
            print("Enter 10 number \n------------------\n ")

            n1 = 0
            odd = 0
            even = 0 
            for i in range(1, 11):
                  n2 = eval(input(f"Enter a number {i}: "))
                  n1 += n2
                  if n2 % 2 == 0:
                        even += n2
                  else:
                        odd += n2

                  print(f"The total of the number you entered is {n1} ")
                  print(f"The total of the EVEN number you entered is {even} ")
                  print(f"The total of the ODD you entered is {odd} ")

      def act13():
            n1 = eval(input("Enter a number: "))
            n2 = 1
            for x in range(n1, 0, -1):
                  print(x)
                  n2 *= x
            print(f"The Factorial of {n1} is {n2}")

      def act14():
            for i in range(0,11):
                  print(i, end="")
                  for k in range(0,11):
                        print("*", end= (""))
                  print()

      def act15():
            for i in range(0, 11):
                  print(i, end=" ")
                  for k in range(0, i):
                        print("*", end= (" "))
                  print()

      def act16():
            for x in range(1, 9, 2):
                  for y in range(7, x-1, -1):
                        print(" ", end=" ")
                  for z in range(x, 0, -1):
                        print(" * ", end=" ")  
                  print()    

            for x in range(1, 9, 2):
                  for y in range(x+2):
                        print(" ", end=" ")
                  for z in range(6, x, -1):
                        print(" * ", end=" ")  
                  print()    

      def act17():
            column= eval(input("enter a number--->"))
            for x in range(1,11):
                  for y in  range(1, column + 1):
                        print(f"{x} x {y} = {x * y}", end= "\t")
            print()

      def act18():
            num = int(input("Enter a number of right triangle: ")) 

            for i in range(1, 6):
                  for r in range(1, num + 1):
                        print(" ", end= " ")
                        for j in range(1, i + 1):
                              print("*", end= " ")
                        for k in range(5, i, -1):
                              print(" ", end= " ") 

                  print()

      def act19():
            contin = True
            count = 0

            while contin == True:
                  name = input("Enter a name: ").upper().strip()

                  if name == "STOP":
                        print("The loop has now stopped")
                        print(f"You have entered {count} number of names")
                        break

                  else:
                        count += 1
                        continue

      def act20():
            isContinue = True
            no = 0

            while isContinue: 
                  ask = input("Would you like to add another triangle [Yes / No]: ").strip().upper()

                  if ask == "NO":
                        print("PROGRAM TERMINATED")
                        break
                  elif ask == "YES":
                        no += 1  
                        for r in range(1, no + 1):  
                              print(f"\nTriangle {r}:")
                              for x in range(1, 5):
                                    for y in range(1, x + 1): 
                                          print(" ", end=" ")
                              for z in range(1, (5 - x) + 1):   
                                    print("*", end=" ")
                              print() 
                  else:
                        print("Invalid input. Please enter 'Yes' or 'No'.")
      def act21():

            tuloy = True
            count = 0

            while tuloy == True:
                  name = input("Please enter a name ---> ")
            
                  if name.lower() == "stop":
                        print("Loop has now stopped")
                        print(f"You have entered {count} number")
                        break
                        tuloy = False
                  else:
                        count += 1
      def act23():

            def add(num1, num2):
                  """This function adds the first number and the second number, returning the sum value."""
                  print(f"The sum of the numbers is ---> {num1 + num2}")

            add(1,5)  

      def act24():
            
            from activity23 import add
            import activity1

            add(21,21)
            activity1

      def act25():
            def list():

                  courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

                  courses.remove("Delete w/o index")
                  courses.pop()
                  courses.append("DHRS")
                  courses.insert(0, "ABELS")

                  print(courses)

            list()
      import sys

                  
      passw = input("Enter your password: ")

      if passw.lower() != "password":
                  print("Access Denied")
                  sys.exit() 

      print("Access Granted")
      print("Enjoy using the System")
      print("=" * 50)
            
      try:
            compile = True

            while compile:

                  print("\n\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
                        "\n\tPrint statements    - [1]"
                        "\n\tVariables/Operators - [2]"
                        "\n\tConditionals        - [3]"
                        "\n\tLoops               - [4]"
                        "\n\tList                - [5]"
                        "\n\tFunctions           - [6]"
                        "\n\tCode_challenges      -[7]")
            

                  num = int(input("\n\n\tSelect a Program: "))

                  if num == 1:
      
                        compile = True

                        while compile:

                              print("\n\tSELECT FROM THE FOLLOWING ACTIVITY BELOW \n\t"
                                    "\n\tActivity1 - [1]"
                                    "\n\tActivity2 - [2]"
                                    "\n\tActivity3 - [3]"
                                    )
                        

                              num2 = int(input("\n\n\tSelect Activity: "))

                              if num2 == 1:
                                    act1()
                                    continue

                              elif num2 == 2:
                                    act2()
                                    continue

                              elif num2 == 3:
                                    act3()
                                    continue

                              
                              elif num2 == 0:
                                    con = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                                    if con == "YES":
                                          print("The program will not be terminated")
                                          print("Thank you for using the program")
                                          break

                                    elif con == "NO":
                                          print("The program will now continue")
                                          continue

                                    else:
                                          print("Wrong Input. Invalid Answer")


                              elif num2 < 0:
                                    print("Wrong Input. Must Be A Positive Number.")
                                    continue

                              else:
                                    print("Wrong Input. Invalid Answer")
                                    continue

            
                  elif num == 2:
                        compile = True

                        while compile:

                              print("\n\tSELECT FROM THE FOLLOWING ACTIVITY BELOW \n\t"
                                    "\n\tActivity4 - [1]"
                                    "\n\tActivity5 - [2]"
                                    "\n\tActivity6 - [3]"
                                    "\n\tActivity7 - [4]"
                                    )
                        

                              num3 = int(input("\n\n\tSelect Activity: "))

                              if num3 == 1:
                                    act4()
                                    continue

                              elif num3 == 2:
                                    act5()
                                    continue

                              elif num3 == 3:
                                    act6()
                                    continue

                              elif num3 == 4:
                                    act7()
                                    continue


                              
                              elif num3 == 0:
                                    con = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                                    if con == "YES":
                                          print("The program will not be terminated")
                                          print("Thank you for using the program")
                                          break

                                    elif con == "NO":
                                          print("The program will now continue")
                                          continue

                                    else:
                                          print("Wrong Input. Invalid Answer")


                              elif num3 < 0:
                                    print("Wrong Input. Must Be A Positive Number.")
                                    continue

                              else:
                                    print("Wrong Input. Invalid Answer")
                                    continue

            
                        continue

                  elif num == 3:
                        while compile:

                              print("\n\tSELECT FROM THE FOLLOWING ACTIVITY BELOW \n\t"
                                    "\n\tActivity8  - [1]"
                                    "\n\tActivity9  - [2]"
                                    "\n\tActivity10 - [3]")
                                    
                              num4 = int(input("\n\n\tSelect Activity: "))

                              if num4 == 1:
                                    act8()
                                    continue

                              elif num4 == 2:
                                    act9()
                                    continue

                              elif num4 == 3:
                                    act10()
                                    continue

                              
                              elif num4 == 0:
                                    con = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                                    if con == "YES":
                                          print("The program will not be terminated")
                                          print("Thank you for using the program")
                                          break

                                    elif con == "NO":
                                          print("The program will now continue")
                                          continue

                                    else:
                                          print("Wrong Input. Invalid Answer")


                              elif num4 < 0:
                                    print("Wrong Input. Must Be A Positive Number.")
                                    continue

                              else:
                                    print("Wrong Input. Invalid Answer")
                                    continue
                        continue

                  elif num == 4:
                        while compile:

                              print("\n\tSELECT FROM THE FOLLOWING ACTIVITY BELOW \n\t"
                                    "\n\tActivity11 - [1]"
                                    "\n\tActivity12 - [2]"
                                    "\n\tActivity13 - [3]"
                                    "\n\tActivity14 - [4]"
                                    "\n\tActivity15 - [5]"
                                    "\n\tActivity16 - [6]"
                                    "\n\tActivity17 - [7]"
                                    "\n\tActivity18 - [8]"
                                    "\n\tActivity19 - [9]"
                                    "\n\tActivity20 - [10]")
                                    
                              num5 = int(input("\n\n\tSelect Activity: "))

                              if num5 == 1:
                                    act11()
                                    continue

                              elif num5 == 2:
                                    act12()
                                    continue

                              elif num5 == 3:
                                    act13()
                                    continue

                              elif num5 == 4:
                                    act14()
                                    continue

                              elif num5 == 5:
                                    act15()
                                    continue

                              elif num5 == 6:
                                    act16()
                                    continue

                              elif num5 == 7:
                                    act17()
                                    continue

                              elif num5 == 8:
                                    act18()
                                    continue

                              elif num5 == 9:
                                    act19()
                                    continue

                              elif num5 == 10:
                                    import activity20
                                    continue
                              

                              
                              elif num5 == 0:
                                    con = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                                    if con == "YES":
                                          print("The program will not be terminated")
                                          print("Thank you for using the program")
                                          break

                                    elif con == "NO":
                                          print("The program will now continue")
                                          continue

                                    else:
                                          print("Wrong Input. Invalid Answer")


                              elif num5 < 0:
                                    print("Wrong Input. Must Be A Positive Number.")
                                    continue

                              else:
                                    print("Wrong Input. Invalid Answer")
                                    continue
                        continue


                  elif num == 5:
                        while compile:

                              print("\n\tSELECT FROM THE FOLLOWING ACTIVITY BELOW \n\t"
                                    "\n\tActivity25  - [1]")
                              
                                    
                              num6 = int(input("\n\n\tSelect Activity: "))

                              if num6 == 1:
                                    import activity25
                                    continue

                              
                              elif num6 == 0:
                                    con = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                                    if con == "YES":
                                          print("The program will not be terminated")
                                          print("Thank you for using the program")
                                          break

                                    elif con == "NO":
                                          print("The program will now continue")
                                          continue

                                    else:
                                          print("Wrong Input. Invalid Answer")


                              elif num6 < 0:
                                    print("Wrong Input. Must Be A Positive Number.")
                                    continue

                              else:
                                    print("Wrong Input. Invalid Answer")
                                    continue
                        continue

      

                  elif num == 6:
                        while compile:

                              print("\n\tSELECT FROM THE FOLLOWING ACTIVITY BELOW \n\t"
                                    "\n\tActivit21  - [1]"
                                    "\n\tActivity23 - [2]"
                                    "\n\tActivity24 - [3]")
                              
                              num7 = int(input("\n\n\tSelect Activity: "))

                              if num7 == 1:
                                    act21()
                                    continue

                              elif num7 == 2:
                                    act23()
                                    continue

                              elif num7 == 3:
                                    act24()
                                    continue

                              elif num7 == 0:
                                    con = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                                    if con == "YES":
                                          print("The program will not be terminated")
                                          print("Thank you for using the program")
                                          break

                                    elif con == "NO":
                                          print("The program will now continue")
                                          continue

                                    else:
                                          print("Wrong Input. Invalid Answer")


                              elif num7 < 0:
                                    print("Wrong Input. Must Be A Positive Number.")
                                    continue

                              else:
                                    print("Wrong Input. Invalid Answer")
                                    continue
                        continue
                  
                  elif num== 7:

                        while compile:

                              print("\n\tSELECT FROM THE FOLLOWING ACTIVITY BELOW \n\t"
                                    "\n\tcode_challenge1 - [1]"
                                    "\n\tcode_challenge2 - [2]"
                                    "\n\tcode_challenge3 - [3]"
                                    "\n\tcode_challenge4 - [4]"
                                    "\n\tcode_challenge5 - [5]"
                                    "\n\tcode_challenge6 - [6]"
                                    "\n\tcode_challenge7 - [7]"
                                    "\n\tcode_challenge8 - [8]"
                                    "\n\tcode_challenge9 - [9]"
                                    "\n\tcode_challenge10- [10]"
                                    "\n\tcode_challenge11- [11]"
                                    "\n\tcode_challenge12- [12]"
                                    "\n\tcode_challenge13- [13]"
                                    "\n\tcode_challenge14- [14]"
                                    "\n\tcode_challenge15- [15]"
                                    "\n\tcode_challenge16- [16]")
                                    
                              num8 = int(input("\n\n\tSelect Activity: "))

                              if num8 == 1:
                                    import code_challenge1
                                    continue

                              elif num8 == 2:
                                    import code_challenge2
                                    continue

                              elif num8 == 3:
                                    act13()
                                    continue

                              elif num8 == 4:
                                    import code_challenge4
                                    continue

                              elif num8 == 5:
                                    import code_challenge5
                                    continue

                              elif num8 == 6:
                                    import code_challenge6
                                    continue

                              elif num8 == 7:
                                    import code_challenge7
                                    continue

                              elif num8 == 8:
                                    import code_challenge8
                                    continue

                              elif num8 == 9:
                                    import code_challenge9
                                    continue

                              elif num8 == 10:
                                    import code_challenge10
                                    continue

                              elif num8 == 11:
                                    import code_challenge11
                                    continue

                              elif num8 == 12:
                                    import code_challenge12
                                    continue

                              elif num8 == 13:
                                    import code_challenge13
                                    continue

                              elif num8 == 14:
                                    import code_challenge14
                                    continue

                              elif num8 == 15:
                                    import code_challenge15
                                    continue

                              elif num8 == 16:
                                    import code_challenge16
                                    continue
                              

                              
                              elif num8 == 0:
                                    con = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                                    if con == "YES":
                                          print("The program will not be terminated")
                                          print("Thank you for using the program")
                                          break

                                    elif con == "NO":
                                          print("The program will now continue")
                                          continue

                                    else:
                                          print("Wrong Input. Invalid Answer")


                              elif num8 < 0:
                                    print("Wrong Input. Must Be A Positive Number.")
                                    continue

                              else:
                                    print("Wrong Input. Invalid Answer")
                                    continue
                        continue
                  
                  
                  
                  elif num == 0:
                        cont = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                        if cont == "YES":
                              print("The program will not be terminated")
                              print("Thank you for using the program")
                              break

                        elif cont == "NO":
                              print("The program will now continue")
                              continue

                        else:
                              print("Wrong Input. Invalid Answer")


                  elif num < 0:
                        print("Wrong Input. Must Be A Positive Number.")
                        continue

                  else:
                        print("Wrong Input. Invalid Answer")
                        continue

      except ValueError:
            print("Wrong Input. Must Be A Number.")
           
act22()



