from asyncore import file_dispatcher
import os
import csv
from tokenize import Double
candidates_poll = {}
candidates = []
votes = []
counter = 0
poll_file = os.path.join("Resources","election_data.csv")
path =  "/Users/tony/Documents/GitHub/python-challenge/PyBank/Resources/election_data.csv"

with open (poll_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    print("Election Results")
    print('-----------------------')

    for row in csv_reader:
        votes.append(row[0]) # import all votes into a list
        candidates.append(row[2])
        counter = counter +1

    for i in candidates:
        if i in candidates_poll.keys():
            candidates_poll[i]=candidates_poll[i]+1
        else: 
            candidates_poll[i] = 1

Khan_vote = candidates_poll['Khan']
Correy_vote = candidates_poll['Correy']
Li_vote = candidates_poll['Li']
Tooley_vote = candidates_poll["O'Tooley"]

Khan_per = Khan_vote/counter
Correy_per = Correy_vote/counter
Li_per = Li_vote/counter
Tooley_per = Tooley_vote/counter

K="{:.2%}".format(Khan_per)
C="{:.2%}".format(Correy_per)
L="{:.2%}".format(Li_per)
T="{:.2%}".format(Tooley_per)


print(f"total votes:{counter}")
print("----------------------")
print(f"Khan: {K} ({candidates_poll['Khan']})")
print(f"Correy: {C} ({candidates_poll['Correy']})")
print(f"Li: {L} ({candidates_poll['Li']})")
#print(f"O'Tooley: {candidates_poll["O'Tooley"]}")
print(candidates_poll)
print("------------------------")

key_list = list(candidates_poll.keys())
value_list = list(candidates_poll.values())
max_1 = max(candidates_poll.values())
position = value_list.index(max_1)
print(f"Winner: {key_list[position]}")
print("-------------------------")