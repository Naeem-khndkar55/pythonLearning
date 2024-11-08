sent = input("Enter Your Sentence; ")
words =sent.split()
word_cnt = {}
for word in words:
    if word in word_cnt:
        word_cnt[word]+=1
    else:
        word_cnt[word]=1   


print(word_cnt)       