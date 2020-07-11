s = input()
firstWord = s[:s.find(' ')]
secondWord = s[s.find(' ') + 1:]
print(secondWord + ' ' + firstWord)
