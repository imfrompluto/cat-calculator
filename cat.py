from ast import Str
# print(2*(3*20+5*20+5*15))

# number = 1
# while number < 101:
    # print(str(number) + "-" + str(number * number))
    # number = number + 1

amount = int(input("how many cats do you have? "))
# print("you have " + amount + " cats ")
food = int(input("how many times does your cat eat a day? "))
# gram = input("how many grams do they eat in one meal? ")
litter = int(input("how often do you clean your cats litter? (in days) "))
toys = int(input("how many toys do you buy for your cat monthly? "))
groom = input("do you take your cat to get groomed? ")

# or one gram
foodprice = 20
litterprice = 20
toyprice = 15
groomprice = 150

# if food == foodprice > 20:

if groom == "no":
    groomprice = 0

if litter < 7 :
    litterprice == 20
else:
    litterprice == 15

if toys < 3 :
    toyprice = 15

else:
    toyprice = 30

result = amount*(food*foodprice+30/litter*litterprice+toys*toyprice+groomprice)
print("you should be spendings £" + str(result) + "!")
    








# finish the program
