def checkIfPan(sentence):
    alphabet = set()

    for letter in sentence:
        if letter not in alphabet:
            alphabet.add(letter)

    return True if len(alphabet) > 25 else False


if __name__ == '__main__':
    print(checkIfPan("thequickbrownfoxjumpsoverthelazydog"))
