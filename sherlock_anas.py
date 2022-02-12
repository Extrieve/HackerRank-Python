from itertools import combinations


def sherlockAndAnagrams(s):
    # Write your code here
    all_combinations = []
    count = 0
    for i in range(1, len(s)):
        combs = list(combinations(s, i))
        print(combs)
        my_dict = dict()
        for item in combs:
            if item not in my_dict:
                my_dict[item] = 1
            else:
                my_dict[item] += 1
                count += 1
                print(item, f'Count: {count}')

    return count


if __name__ == '__main__':
    word = input()
    print(sherlockAndAnagrams(word))
