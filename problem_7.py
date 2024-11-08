# code for findig the longest string in the sentence

str = input("Enter Your Sentence: ")
str_word= str.split()
length =0
for word in str_word :
    if(len(word)>length):
        length=len(word)
        logest_word =word


print(f" The Longest word is: {logest_word}")