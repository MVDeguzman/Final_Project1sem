pre = eval(input("please enter your grades in prrelim: "))
mid = eval(input("please enter your grades in mid term: "))
semi = eval(input("please enter your grades semi finals: "))
final = eval(input("please enter your grades in finals: "))
quiz = eval(input("please enter your grades in your quiz: "))
project = eval(input("please enter your grades in your final project: "))

pre *.15
mid *.15 
semi *.15 
final *.15 
quiz *.25
project *.15 

if pre > 100 or pre < 74:
 print("you failed")

elif pre > 74 or pre <=100:
 print("you passed the prelim.")
    

if pre >= 100:
    print("you passed the prelim")

else:
    print("you failed")

if mid >= 100: 
    print("you passed the mid term")

else:
    print("you failed")


if semi >= 100: 
    print("you passed the semi final")

else:
    print("you failed")

if final >= 100: 
    print("you passed the fianal")

else:
    print("you failed")

if quiz >= 100: 
    print("you passed the quiz")

else:
    print("you failed")

if project >= 100: 
    print("you passed you final project")

else:
    print("you failed")



