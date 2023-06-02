string = 'Hello, you need to print words which starts with s only in this sentence.'

for word in string.split():
    if word[0] == 's':
        print(word)
