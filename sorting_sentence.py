def sortSentence(s):
        stringlist = s.split(' ')
        stringlist = sorted(stringlist, key=lambda x: x[-1])
        print(stringlist)
        cleanstring = ''
        for i, value in enumerate(stringlist):
            cleanstring += value[:-1]
            if(i < len(stringlist) - 1):
                cleanstring += ' '
        return cleanstring

print(sortSentence('is2 sentence4 This1 a3'))
