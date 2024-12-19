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