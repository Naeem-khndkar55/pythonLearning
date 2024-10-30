res = int(input("Enter the result: "))

if res >= 90:
    print("A+")
elif res < 90 and res >= 70:
    print("A-")
elif res < 70 and res >= 50:
    print("B")
else:
    print("Fail!")
