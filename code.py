# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#print(data)
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
first_innings_delivery = data['innings'][0]['1st innings']['deliveries']

count=0
for deli in first_innings_delivery:
    key = deli.keys()
    for key in deli:
        if deli[key]['batsman'] == 'SC Ganguly':
            count+=1
print('Deliveries faced by SC Ganguly',count)

#  Who was man of the match and how many runs did he scored ?
mom = data['info']['player_of_match'][0]

print('Man of the Match',mom)
runs_scored = 0
for deli in first_innings_delivery:
    for key in deli:
        if deli[key]['batsman'] == mom:
            runs_scored += deli[key]['runs']['batsman']

print('Man of the Match scored',runs_scored)
#  Which batsman played in the first inning?
all_batsman = []
all_non_striker = []
for deli in first_innings_delivery:
    for key in deli:
        all_batsman.append(deli[key]['batsman'])
        all_non_striker.append(deli[key]['non_striker'])

#print(set(all_non_striker))
#print('Batsman played',set(all_batsman))

striker = set(all_batsman)
nonstriker = set(all_non_striker)
uni = striker.union(nonstriker)
print('Batsman played in first innings')
print(uni)

# Which batsman had the most no. of sixes in first inning ?
batsman_hit_sixes = []

for deli in first_innings_delivery:
    for key in deli:
        if deli[key]['runs']['batsman'] == 6:
            batsman_hit_sixes.append(deli[key]['batsman'])

#print(batsman_hit_sixes)

count_sixer = {}
for set_batsman in set(batsman_hit_sixes):
    count_sixer[set_batsman] = 0 #{'RT Pointing' : 0 , 'BB McCullum' : 0}

    for list_batsman in batsman_hit_sixes:
        if list_batsman == set_batsman:
            count_sixer[set_batsman] +=1


#print(max(count_sixer.values()))
print(max(count_sixer, key=count_sixer.get))

#from collections import Counter
#Counter(batsman_hit_sixes).most_common(1)
# Find the names of all players that got bowled out in the second innings.
second_innings_delivery = data['innings'][1]['2nd innings']['deliveries']
bowled_players = []

for deli in second_innings_delivery:
    for key in deli:
        if 'wicket' in deli[key].keys() and deli[key]['wicket']['kind']=='bowled':
            bowled_players.append(deli[key]['batsman'])
print(bowled_players)



# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extra_1st_innings = []
for deli in first_innings_delivery:
    for key in deli:
        if 'extras' in deli[key]:
            extra_1st_innings.append(deli[key])


len(extra_1st_innings)
extra_2nd_innings = [
    deli[key]
    for deli in second_innings_delivery for key in deli if 'extras' in deli[key]
]

len(extra_2nd_innings) - len(extra_1st_innings)


# Code ends here


