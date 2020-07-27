inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()

for line in range(len(lines)):
    if lines[line] == 'VOTES:\n':
        votes_string = line

parties = []

for line in range(1, votes_string):
    parties.append(lines[line].rstrip())

votes = []

for line in range(votes_string + 1, len(lines)):
    votes.append(lines[line].rstrip())

count_votes = []

for vote in parties:
    count_votes.append(votes.count(vote))

summ_votes = 0

for num in count_votes:
    summ_votes += num

percent = []

for num in count_votes:
    p = round(num / summ_votes, 3)
    percent.append(p)

percent_and_title = []
for subj in range(len(parties)):
    percent_and_title.append([percent[subj], parties[subj]])
percent_and_title.sort(key=lambda x: (-x[0], x[1]))
for i in range(len(percent_and_title)):
    print(percent_and_title[i][1])
