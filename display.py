import csv

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

with open('matchups.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(reader)
    for row in reader:
        char1 = chars_short[int(row[0])]
        char2 = chars_short[int(row[1])]
        num_matches = int(row[2])
        p1_win_rate = float(row[3])
        p2_win_rate = float(row[4])
        score = int(row[5])
        if score > 0:
            print(f"{char1} vs {char2}: +{score}")
        else:
            print(f"{char1} vs {char2}: {score}")
