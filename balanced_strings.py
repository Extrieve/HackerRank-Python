def balancedStringSplit(s: str) -> int:
    lCounter, rCounter = 0, 0
    perfectStrings = 0
    for value in s:
        if(value == 'L'):
            lCounter += 1
            if(lCounter == rCounter and lCounter != 0):
                perfectStrings += 1
                lCounter = 0
                rCounter = 0
        else:
            rCounter += 1
            if(lCounter == rCounter and lCounter != 0):
                perfectStrings += 1
                lCounter = 0
                rCounter = 0

    return perfectStrings

print(balancedStringSplit('RLRRLLRLRL'))
