word = 'ac'

def longest_pal_substring(my_input):
    ans = ''
    for i in range(len(my_input)):
        candidate = ''
        for next_letter in my_input[i:]:
            candidate += next_letter
            if candidate == candidate[::-1] and len(candidate) > len(ans):
                ans = candidate

    return ans


print(longest_pal_substring(word))