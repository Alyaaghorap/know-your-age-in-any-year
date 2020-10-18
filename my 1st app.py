

name = input("hi, type ur name please")
print(" oh! that's such an awesome name," + format(name))
print("this program detects your own age in a certain year you will choose")
age = int(input("would you please tell me your current age?"))
year = int(input("now choose the year you wish to now your age in"))
Cyear = int(input("enter the current year"))
if year >= Cyear:
    print("your age will be {}".format(age + (year - Cyear)))
else:
    print("your age was {}".format(age - (Cyear - year)))




