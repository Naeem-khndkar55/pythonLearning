
# code for counting the vowel and consonent in the string;

str = input("Enter your String: ")
str.lower()

vowel ="aeiou"
total_v=0
total_c =0
for c in str:
 if c.isalpha():
    if c in vowel:
      total_v+=1
    else:
      total_c+=1  
print("Total Vowel is : {} and Total Consonent is {}".format(total_v,total_c))     
