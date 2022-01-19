def checkIfPan(sentence):
    alphabet = dict()

    for letter in sentence:
        if letter not in alphabet:
            alphabet[letter] = 1

    return True if len(alphabet) > 25 else False


if __name__ == '__main__':
    print(checkIfPan("thequickbrownfoxjumpsoverthelazydog"))
