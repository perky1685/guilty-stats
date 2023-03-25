import csv
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

floor = 99

win_rates = []
for i in range(len(chars_long)):
    character = chars_long[i]
    char_id = i
    win_rate = get_win_rate(char_id, floor)
    win_rates.append((character, win_rate))

# Sort the win rates in descending order based on the win rate
sorted_win_rates = sorted(win_rates, key=lambda x: x[1], reverse=True)

# Write the win rates to a CSV file
with open(f"floor{floor}.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Character", "Win Rate"])
    for character, win_rate in sorted_win_rates:
        writer.writerow([character, win_rate])
