def countMatches(items, ruleKey, ruleValue):
    list = ['type', 'color', 'name']
    ruleIndex = list.index(ruleKey)
    exclusive = [item for item in items if ruleValue == item[:][ruleIndex]]

    return len(exclusive)

print(countMatches([["ii","iiiiiii","ii"],["iiiiiii","iiiiiii","ii"],["ii","iiiiiii","iiiiiii"]], 'color', 'ii'))
