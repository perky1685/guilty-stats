import psycopg2

def get_win_rate(char_id, floor):
    conn = psycopg2.connect(
        host="localhost",
        database="ggst-stats",
        user="postgres",
        password="password"
    )

    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM match_temp WHERE (player1_char = {char_id} OR player2_char = {char_id}) AND floor = {floor}")
    total_matches = cur.fetchone()[0]
    cur.execute(f"SELECT COUNT(*) FROM match_temp WHERE (winner = 1 AND player1_char = {char_id} OR winner = 2 AND player2_char = {char_id}) AND floor = {floor}")
    wins = cur.fetchone()[0]

    win_rate = (wins / total_matches) * 100
    return win_rate


chars_short = ("SO","KY","MA","AX","CH","PO","FA","MI","ZA","RA","LE","NA","GI","AN","IN","GO","JC","HA","BA","TE","BI","SI")
chars_long = ("Sol Badguy", "Ky Kiske", "May", "Axl Low", "Chipp", "Potemkin", "Faust", "Millia", "Zato=1", "Ramlethal", "Leo Whitefang", "Nagoriyuki", "Anji Mito", "Ino", "Giovanna", "Jack-O", "Happy Chaos", "Baiken", "Testament", "Brisket", "Sin Kiske")

print("Please enter floor:")
floor = input()
print("Please wait up to 15 seconds...")

win_rates = []
for i in range(len(chars_long)):
    character = chars_long[i]
    char_id = i
    win_rate = get_win_rate(char_id, floor)
    win_rates.append((character, win_rate))

# Sort the win rates in descending order based on the win rate
sorted_win_rates = sorted(win_rates, key=lambda x: x[1], reverse=True)

for character, win_rate in sorted_win_rates:
    if floor != "99":
        print(f"Win rate for {character} on floor {floor}: {round(win_rate, 2)}%")
    else:
        print(f"Win rate for {character} in the Celestial floor: {round(win_rate, 2)}%")
