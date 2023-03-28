import psycopg2
import csv
import os

def write_all_matchups():
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
        UNION
        SELECT 
            player1_char, 
            player2_char, 
            COUNT(*) AS num_matches, 
            50.00 AS player1_win_rate, 
            50.00 AS player2_win_rate
        FROM 
            matches 
        WHERE 
            player1_char = player2_char 
        GROUP BY 
            player1_char, 
            player2_char
        ORDER BY 
            player1_char, 
            player2_char
    """
    chars_short = ("SO","KY","MA","AX","CH","PO","FA","MI","ZA","RA","LE","NA","GI","AN","IN","GO","JC","HA","BA","TE","BI","SI")
    # Execute the query and fetch the results
    with conn.cursor() as cur:
        cur.execute(query)
        results = cur.fetchall()
    # Process the results and write them to a CSV file
    with open("allfloors.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Character 1", "Character 2", "Num Matches", "Player 1 Win Rate", "Player 2 Win Rate", "Score"])
        for row in results:
            player1_char, player2_char, num_matches, player1_win_rate, player2_win_rate = row
            if player1_char == player2_char:
                score = "99"
            else:
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
                try:
                    writer.writerow([chars_short[player1_char], chars_short[player2_char], num_matches, player1_win_rate, player2_win_rate, score])
                except:
                    pass

def matchup_by_floor(floor):
    conn = psycopg2.connect(
        host="localhost",
        database="ggst-stats",
        user="postgres",
        password="password"
    )

    # Define the SQL query to fetch the matchups and win rates for each character
    query = f"""
    SELECT
        player1_char, 
        player2_char, 
        floor, 
        COUNT(*) AS num_matches, 
        ROUND(COUNT(CASE WHEN winner = 1 THEN 1 END)::numeric / COUNT(*) * 100, 2) AS player1_win_rate, 
        ROUND(COUNT(CASE WHEN winner = 2 THEN 1 END)::numeric / COUNT(*) * 100, 2) AS player2_win_rate
    FROM 
        matches 
    WHERE 
        player1_char != player2_char 
        AND floor = {floor} -- Replace with desired floor number
    GROUP BY 
        player1_char, 
        player2_char, 
        floor
    UNION
    SELECT 
        player1_char, 
        player2_char, 
        floor, 
        COUNT(*) AS num_matches, 
        50.00 AS player1_win_rate, 
        50.00 AS player2_win_rate
    FROM 
        matches 
    WHERE 
        player1_char = player2_char 
        AND floor = {floor} -- Replace with desired floor number
    GROUP BY 
        player1_char, 
        player2_char, 
        floor
    ORDER BY 
        player1_char, 
        player2_char, 
        floor 
        """
    chars_short = ("SO","KY","MA","AX","CH","PO","FA","MI","ZA","RA","LE","NA","GI","AN","IN","GO","JC","HA","BA","TE","BI","SI")

    # Execute the query and fetch the results
    with conn.cursor() as cur:
        cur.execute(query)
        results = cur.fetchall()
        if not os.path.exists("matchup"):
            os.makedirs("matchup")
        with open(f"matchup/floor{floor}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Character 1", "Character 2", "Floor", "Num Matches", "Player 1 Win Rate", "Player 2 Win Rate", "Score"])
            for row in results:
                player1_char, player2_char, floor, num_matches, player1_win_rate, player2_win_rate = row
                if player1_char == player2_char:
                    score = "99"
                else:
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
                    try:
                        writer.writerow([chars_short[player1_char], chars_short[player2_char], num_matches, player1_win_rate, player2_win_rate, score])
                    except:
                        pass

# Prompt user for the floor number to filter by
#floor = input("What floor would you like to get the matchups of? ")

#### Call the function with the provided floor number
#for x in range (1, 11):
#    matchup_by_floor(x)
#matchup_by_floor(99)
write_all_matchups()