# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

    if m == 0:
        return f"{nums[h]} o' clock"
    elif m == 1:
        return f'{nums[m]} minute past {nums[h]}'
    elif m == 15:
        return f'quarter past {nums[h]}'
    elif m == 30:
        return f'half past {nums[h]}'
    elif m == 45:
        return f'quarter to {nums[h+1]}'
    elif m > 0 and m < 30:
        return f'{nums[m]} minutes past {nums[h]}'
    else:
        return f'{nums[len(nums) - (m % len(nums))]} minutes to {nums[h+1]}'


if __name__ == '__main__':
    print(timeInWords(1, 1))
