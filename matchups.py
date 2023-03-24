import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="ggst-stats",
    user="postgres",
    password="password"
)

# Define the SQL query to fetch the matchups and win rates for each character
query = """
    SELECT 
        player1_char, 
        player2_char, 
        COUNT(*) AS num_matches, 
        ROUND(COUNT(CASE WHEN winner = 1 THEN 1 END)::numeric / COUNT(*) * 100, 2) AS player1_win_rate, 
        ROUND(COUNT(CASE WHEN winner = 2 THEN 1 END)::numeric / COUNT(*) * 100, 2) AS player2_win_rate
    FROM 
        matches 
    WHERE 
        player1_char != player2_char 
    GROUP BY 
        player1_char, 
        player2_char
    ORDER BY 
        player1_char, 
        player2_char
"""

# Execute the query and fetch the results
with conn.cursor() as cur:
    cur.execute(query)
    results = cur.fetchall()

# Process the results and write them to a CSV file
with open("matchups.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Character 1", "Character 2", "Num Matches", "Player 1 Win Rate", "Player 2 Win Rate", "Score"])
    for row in results:
        player1_char, player2_char, num_matches, player1_win_rate, player2_win_rate = row
        win_rate_diff = player1_win_rate - player2_win_rate
        if win_rate_diff > 10:
            score = "+3"
        elif win_rate_diff > 5:
            score = "+2"
        elif win_rate_diff > 2.5:
            score = "+1"
        elif win_rate_diff < -10:
            score = "-3"
        elif win_rate_diff < -5:
            score = "-2"
        elif win_rate_diff < -2.5:
            score = "-1"
        else:
            score = "0"
        writer.writerow([player1_char, player2_char, num_matches, player1_win_rate, player2_win_rate, score])