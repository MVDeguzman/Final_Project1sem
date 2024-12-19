import sys

# Password verification
passw = input("Enter your password: ")

if passw.lower() != "password":
    print("Access Denied")
    sys.exit()  # Terminate the program if the password is incorrect

print("Access Granted")
print("Enjoy using the System")
print("=" * 50)

# Main Program

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
              "\n\tCode_challenge      - [7]")

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

        # Add more program options as needed...

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

