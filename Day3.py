# Odd and even
# a=int(input("Please enter your number\n"))
# if a%2==0:
#     print("Your number is even")
# else:
#     print("Your number is odd")

#
# h=float(input("Enter your heigth\n"))
# if h>=120:
#     print("You can ride")
#     age=int(input("Enter your Age:\n"))
#     if age>=18:
#         print("You Have to pay the $18")
#     elif age in range (9,15):
#         print("You have to pay $12")
#     else:
#         print("You Have to pay the $6")
# else:
#     print("Try again next time...")

# Program to write body mass
# Formula=Weight/height*hight
# weight=float(input("Enter your weight: \n"))
# height=float(input("Enter your Height: \n"))
# bmi=weight//height**2
# print(f"BMI={bmi}")
# if bmi<18.5:
#     print(f"Your BMI is {bmi},Your are sightly underweight")
# elif 18.5 < bmi<25:
#     print(f"Your BMI is {bmi},Your are normal weight")
# elif 25<bmi<30:
#     print(f"Your BMI is {bmi},Your are sightly overweight")
# elif 30<bmi<35:
#     print(f"Your BMI is {bmi},Your are obese")
# elif bmi>35:
#     print(f"your bmi is {bmi},your clinically obese")

#leap year
year=int(input("Please enter you year that you want to check!!\n"))
if year%4==0:
    if year%100==0:
        if (year%400==0):
            print("Your year is leap")
        else:
            print("Your year is not leap")
    else:
        print("Your year is leap")
else:
    print("Your year is leap")



