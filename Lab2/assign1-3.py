"""Write a program that asks the user to enter a length in feet. The program should then give the user the option to convert from
 feet into inches, yards, miles, millimeters, centimeters, meters, or kilometers. Say if the user enters a 1, then the program
   converts to inches, if they enter a 2, then the program converts to yards, etc. While this can be done with if statements, it
     is much shorter with lists and it is also easier to add new conversions if you use lists."""

print(" options available")
print(" 1-inches")
print("2-yards")
print(" 3-miles")
print("4-millimeters")
print("5-centimeters")
print("6-meters")
print("7-kilometers")
length=int(input("enter the length in feet"))
option=int(input("enter the number corresponding to conversion"))
conversion_list=[12,0.33, 0.000189, 304.8 ,30.48,0.3048,0.000305 ]
result=length*conversion_list[option-1]
print("length after conversion is",result)
