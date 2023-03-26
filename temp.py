chars = ("SO","KY","MA","AX","CH","PO","FA","MI","ZA","RA","LE","NA","GI","AN","IN","GO","JC","HA","BA","TE","BI","SI")

# create a new file with the .py extension
with open("characters.py", "w") as f:
    # write import statement to the file
    f.write("from flask import render_template, Blueprint, request\n")
    f.write("import get_win_rates\n\n")
    # create a new Flask Blueprint
    f.write("views = Blueprint(\"views\", __name__)\n\n")
    # iterate through each character
    for char in chars:
        # write Python code for the function to the file
        f.write(f"@views.route(\"/{char}\", methods=[\"GET\", \"POST\"])\n")
        f.write(f"def {char}():\n")
        f.write("    win_rate_req = []\n")
        f.write("    pick_rate_req = []\n")
        f.write("    matchup_req = []\n")
        f.write("    bad_matchups = []\n")
        f.write("    floor = None\n")
        f.write("    if request.method == \"POST\":\n")
        f.write("        floor = int(request.form[\"floor\"])\n")
        f.write("        win_rate_req = get_win_rates.get_win_rates(floor)\n")
        f.write("        pick_rate_req = get_win_rates.get_pick_rates(floor)\n")
        f.write("        matchup_req = get_win_rates.get_matchups(floor)\n")
        f.write(f"    return render_template(\"character/{char}.html\", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)\n\n")

print("Python file created!")
