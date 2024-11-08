url = input("Enter the URL: ")

key_word = url.split("/");

p = len(key_word);

desire = key_word[p-1];
print(f"The file Name is: {desire}")