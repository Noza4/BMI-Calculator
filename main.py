from calculation import calculate, status, save_record
from error import IncorrectMass

name = input("Enter Your Name: ")

correct = False
while correct is False:
    try:
        kg = float(input("Enter Your Weight: "))
        if kg < 5:
            raise IncorrectMass
        else:
            correct = True
    except IncorrectMass:
        print("Weight You Entered is invalid")


str_hg = str(input("Enter Your Height: "))

hg = float(str_hg)

if "." not in str_hg:
    hg = hg / 100

bmi = calculate(kg, hg)

status = status(bmi)

print(f"Your BMI is {bmi} and for this index your status is {status}")

save_record(name, bmi, status)



