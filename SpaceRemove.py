# Remove leading and trailing spaces and replace multiple spaces with a single space
sentence = input("Enter a sentence with extra spaces: ")
cleaned_sentence = ' '.join(sentence.split())

print(f"Original: '{sentence}'")
print(f"Cleaned: '{cleaned_sentence}'")
    