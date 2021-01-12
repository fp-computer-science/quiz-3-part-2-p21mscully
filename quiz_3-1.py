# Author MRS 1/12/21

younglings = ['Petro', 'Katooni', 'Byph', 'Ganodi', 'Zatt', 'Gungi']
race = ['Human', 'Tholothian', 'Ithorian', 'Rodian', 'Nautolan', 'Wookie']

def find_youngling(younglings, race):
    for index, names in enumerate(younglings):
        younglings[index] = names + str(race[:1])
        return younglings

print(find_youngling)