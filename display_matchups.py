import csv

# dictionary to turn number into character
chars_short = {
    0: "SO",
    1: "KY",
    2: "MA",
    3: "AX",
    4: "CH",
    5: "PO",
    6: "FA",
    7: "MI",
    8: "ZA",
    9: "RA",
    10: "LE",
    11: "NA",
    12: "GI",
    13: "AN",
    14: "IN",
    15: "GO",
    16: "JC",
    17: "HA",
    18: "BA",
    19: "TE",
    20: "BI",
    21: "SI"
}


def get_all_matchups(chars_short):
    matchups = []
    with open('allfloors.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = next(reader)
        for row in reader:
            char1 = chars_short[int(row[0])]
            char2 = chars_short[int(row[1])]
            num_matches = int(row[2])
            p1_win_rate = float(row[3])
            p2_win_rate = float(row[4])
            score = int(row[5])
            matchups.append((char1, char2, num_matches, p1_win_rate, p2_win_rate, score))
    return matchups

matchups = get_all_matchups(chars_short)
print("which character matchups would you like ")
character_choice = input()

for matchup in matchups:
    char1, char2, num_matches, p1_win_rate, p2_win_rate, score = matchup
    if char1 == chars_short[int(character_choice)]:
        if score == 99:
            print(f"{char1} ditto")
        elif score > 0:
            print(f"{char1} vs {char2}: +{score}")
        else:
            print(f"{char1} vs {char2}: {score}")