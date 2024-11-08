# code for checking if the string is palindrom or not

str = input("Enter your string: ")
str.strip()
str.lower
str2=str[::-1]
if(str == str2):
    print(f"the  string : {str} is a palindrom string")
else:
    print(f"the string : {str} is not a palindrom string")    