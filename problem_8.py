# code for deleting the duplicate eliments from a string
str = input("enter Your string: ")
str.lower()
unique_element=set()
res=""
for c in str:
    if c.isalpha():
       if c not in unique_element:
           unique_element.add(c)
           res+=c



print(f"the new string is: {res}")
