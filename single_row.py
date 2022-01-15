# There is a special keyboard with all keys in a single row.
# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25).
# Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character.
# The time taken to move your finger from index i to index j is |i - j|.
# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

def calculateTime(keyboard, word):
    position = 'a'
    total = 0
    for letter in word:
        total += abs(ord(position) - ord(letter))
        position = letter
    return total


def calculateTime1(keyboard, word):
    position = keyboard[0]
    total = 0
    for letter in word:
        total += abs(keyboard.index(letter) - keyboard.index(position))
        position = letter
    return total


if __name__ == '__main__':
    print(calculateTime1('pqrstuvwxyzabcdefghijklmno', 'leetcode'))
