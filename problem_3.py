m= int(input("Enter your number: "))

if m%3==0 and m%5==0: 
    print("FizzBuzz")
elif m%3==0:
    print("Fizz")
elif m%5==0:
    print("Buzz")
else :
    print("Not a FizzBuzz Number")