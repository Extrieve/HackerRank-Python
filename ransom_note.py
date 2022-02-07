def checkMagazine(magazine, note):
    # Write your code here
    magazine_dict = {item: magazine.count(item) for item in magazine}
    # note_dict = dict.fromkeys(note)
    complete_letters = True
    for word in note:
        if word not in magazine_dict:
            complete_letters = False
            break
        else:
            if magazine_dict[word] < 1:
                complete_letters = False
                break
            else:
                magazine_dict[word] -= 1

    return 'Yes' if complete_letters else 'No'


def checkMagazine1(magazine, note):
    # Write your code here
    complete = True
    for word in note:
        if word not in magazine:
            complete = False
            break
        else:
            magazine.remove(word)
    return 'Yes' if complete else 'No'


if __name__ == '__main__':
    n = input()
    magazine = input().split()
    note = input().split()

    print(checkMagazine1(magazine, note))
