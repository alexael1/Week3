#num = int(input("Enter a number"))
#for i in range (1,11):
  #  if i ==2:
 #       continue
  #  print(num, "*", i, "=", num *i)
  
  
#for letter in "Alexoaie":
#    if letter == "a":     
#        continue   
#    print(letter)


while True:
    print("Press 1 for addition")
    print("Print 2 for substraction")
    print("Print 3 for Exit")
    choice = int(input("Enter your input: "))
    if choice == 1:
        print("Add function")
    elif choice == 2:
        print("Substract function")
    elif choice == 3:
        print("exit")
        break
    else:
        print("Try correct number")