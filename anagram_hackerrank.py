def anagram(s):
    # Write your code here
    length = len(s)
    if length % 2 != 0:
        return -1

    # s1, s2 = [letter for letter in sorted(s[:length//2])], [
    #     letter for letter in sorted(s[length//2:])]

    s1 = s[:length//2]
    s2 = s[length//2:]
    print(f'THIS IS S1: {s1}\nTHIS IS S2: {s2}\n')
    s1_dict = dict()
    s2_dict = dict()

    for i in range(length//2):
        if s1[i] not in s1_dict:
            s1_dict[s1[i]] = 1
        else:
            s1_dict[s1[i]] += 1
    
        if s2[i] not in s2_dict:
            s2_dict[s2[i]] = 1
        else:
            s2_dict[s2[i]] += 1

    first_count = 0
    for letter in s1_dict.items():
        if letter[0] not in s2_dict:
            first_count += letter[1]
        elif letter[0] in s2_dict and s2_dict[letter[0]] > letter[1]:
            first_count += s2_dict[letter[0]] - letter[1]

    second_count = 0
    for letter in s2_dict.items():
        if letter[0] not in s1_dict:
            second_count += letter[1]
        elif letter[0] in s1_dict and s1_dict[letter[0]] > letter[1]:
            second_count += s1_dict[letter[0]] - letter[1]

    return first_count if first_count < second_count else second_count


def anagram1(s):
    length = len(s)
    if length % 2 != 0:
        return -1

    s1 = sorted(s[:length//2])
    s2 = sorted(s[length//2:])
    count = 0

    for letter in s1:
        if letter not in s2:
            count += 1
        elif letter in s2:
            temp = s1.count(letter) - s2.count(letter)
            count += temp if temp > 0 else 0
    
    return count

if __name__ == '__main__':

    word = input()
    print(anagram1(word))
