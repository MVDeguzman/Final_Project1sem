pre = eval(input("enter your grade in prelim: "))
mid = eval(input("enter your grade in mid term: "))
semi = eval(input("enter your grade in semi final: "))
final = eval(input("enter your grade in final: "))
quiz = eval(input("enter your grade in quiz: "))
project = eval(input("enter your grade in fianl project: "))


if (pre >= 65 and pre <= 100) and (mid >= 65 and mid <= 100) and (semi >= 65 and semi <= 100) and (final >= 65 and final <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
 
    fg = (pre*0.15)+(mid*0.15)+(semi*0.15)+(final*0.15)+(quiz*0.25)+(project*0.15)

    if fg >= 74:
        print(" congrats, you passed the course.")
 
    else:
        print("you failed the subject.")

else:
 print("error.")