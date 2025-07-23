import string

text = input("Введите предложение:")

for char in string.punctuation + " ":
    text = text.replace(char, "")
words = text.title()
hashtag = "#" + words

if len(hashtag) > 140 :
    hashtag = hashtag[:140]

print(hashtag)
