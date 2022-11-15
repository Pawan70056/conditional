num=int(input("Enter any number: "))
if num%3==0 and num%5==0:
    print("it is fizzbuzz")
elif num%3==0:
    print("it is Fuzz")
elif num%5==0:
    print("it is fz")
else:
    print("it is not divisible number")


