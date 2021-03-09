# - Reverse only words with 5 or more letters
def spin_words(sentence):
    old = sentence.split(' ')
    new = list()
    for w in old:
        if len(w) >= 5:
            new.append(w[::-1])
        else:
            new.append(w)
    print(' '.join(new))


spin_words('Welcome')
spin_words('to')
spin_words('Hey fellow warriors')