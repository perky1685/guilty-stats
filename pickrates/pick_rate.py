import psycopg2
import numpy as np
from decimal import Decimal
import csv

conn = psycopg2.connect(
    host="localhost",
    database="ggst-stats",
    user="postgres",
    password="password"
)

#chars = ("SO","KY","MA","AX","CH","PO","FA","MI","ZA","RA","LE","NA","GI","AN","IN","GO","JC","HA","BA","TE","BI","SI")
chars_long = ("Sol Badguy", "Ky Kiske", "May", "Axl Low", "Chipp", "Potemkin", "Faust", "Millia", "Zato=1", "Ramlethal", "Leo Whitefang", "Nagoriyuki", "Anji Mito", "Ino", "Giovanna", "Jack-O", "Happy Chaos", "Baiken", "Testament", "Brisket", "Sin Kiske")

p1char_count = [0] * len(chars_long)
p2char_count = [0] * len(chars_long)

def get_p1char_count(chars, p1char_count):
    # get every player one character form the database
    cur = conn.cursor()
    cur.execute("SELECT player1_char FROM match_temp")
    rows = cur.fetchall()

    # updates the character count every time that character is found
    for row in rows:
        char_index = row[0]
        if char_index < len(chars):
            p1char_count[char_index] += 1
    ### Print the amount per character
    # for i in range(len(chars)):
    #     print(f"{chars[i]}: {p1char_count[i]}")
    cur.close()
    return p1char_count

def get_p2char_count(chars, p2char_count):
    # get every player 2 character from the database
    cur = conn.cursor()
    cur.execute("SELECT player2_char FROM match_temp")
    rows = cur.fetchall()

    # updates the character count every time that character is found
    for row in rows:
        char_index = row[0]
        if char_index < len(chars):
            p2char_count[char_index] += 1
    ### Print the amount per character
    # for i in range(len(chars)):
    #     print(f"{chars[i]}: {p2char_count[i]}")
    cur.close()
    return p2char_count

def print_char_pick_rates(chars, p1char_count, p2char_count):
    # sum(p2char_count) = sum(p1char_count)
    total_games = sum(p1char_count)
    for x in range(len(chars)):
        # had to make it decimal because it wouldnt round properly
        # you can only use decimal on ints not numpy numbers, hence the cast to int
        # prints total pick rate, pick rate on player 1, pick rate on player 2
        p1_percent = Decimal(int(p1char_count[x])) / Decimal(int(total_games)) * Decimal(100)
        p2_percent = Decimal(int(p2char_count[x])) / Decimal(int(total_games)) * Decimal(100)
        total_percent = p1_percent + p2_percent
        print(f"{chars[x]}: {total_percent:.2f}% \n(P1: {p1_percent:.2f}%, P2: {p2_percent:.2f}%)")
        # prints the percentage chance that a character will be on either side if that character is picked at all
        total_chars = p1char_count[x] + p2char_count[x]
        p1_percent_char = Decimal(int(p1char_count[x])) / Decimal(int(total_chars)) * Decimal(100)
        p2_percent_char = Decimal(int(p2char_count[x])) / Decimal(int(total_chars)) * Decimal(100)
        print(f"(P1: {p1_percent_char:.2f}%, P2: {p2_percent_char:.2f}%)")

def get_floor_pick_rates(floor_num, chars, p1char_count, p2char_count):
    conn = psycopg2.connect(
        host="localhost",
        database="ggst-stats",
        user="postgres",
        password="password"
    )

    cur = conn.cursor()
    cur.execute(f"SELECT player1_char, player2_char FROM matches WHERE floor = {floor_num}")
    rows = cur.fetchall()

    for row in rows:
        p1char_count[row[0]-1] += 1
        p2char_count[row[1]-1] += 1

    total_games = sum(p1char_count)

    results = []
    for x in range(len(chars)):
        cur.execute(f"SELECT COUNT(*) FROM matches WHERE (player1_char = {x} OR player2_char = {x}) AND floor = {floor_num}")
        total_count = cur.fetchone()[0]
        p1_percent = Decimal(int(p1char_count[x])) / Decimal(int(total_games)) * Decimal(100)
        p2_percent = Decimal(int(p2char_count[x])) / Decimal(int(total_games)) * Decimal(100)
        total_percent = p1_percent + p2_percent
        results.append((chars[x], total_percent, p1_percent, p2_percent, total_count))

    print(f"Floor {floor_num} character pick rates:")
    print_char_pick_rates(chars, p1char_count, p2char_count)
    
    # Save results to CSV file
    with open(f"pickrates/floor{floor_num}.csv", 'w', newline='') as csvfile:
        fieldnames = ['Character', 'Total pick rate', 'P1 pick rate', 'P2 pick rate', 'Raw Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow({'Character': result[0], 'Total pick rate': round(result[1], 2) / 2, 
                             'P1 pick rate': round(result[2], 2), 'P2 pick rate': round(result[3], 2),
                             'Raw Count': result[4]})
    return results

def get_total_char_count(char_index):
    conn = psycopg2.connect(
        host="localhost",
        database="ggst-stats",
        user="postgres",
        password="password"
    )

    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM match_temp WHERE player1_char = {char_index} OR player2_char = {char_index}")
    count = cur.fetchone()[0]
    cur.close()
    return count
#get_p1char_count(chars, p1char_count)
#get_p2char_count(chars, p2char_count)
total_games = np.sum(p1char_count)

for floor_num in range(1, 11):
    get_floor_pick_rates(floor_num, chars_long, p1char_count, p2char_count)
#results = get_floor_pick_rates(floor_num, chars)

conn.close()