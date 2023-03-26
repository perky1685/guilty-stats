from flask import Blueprint, render_template, request
import get_win_rates
import csv

chars_short = ("SO","KY","MA","AX","CH","PO","FA","MI","ZA","RA","LE","NA","GI","AN","IN","GO","JC","HA","BA","TE","BI","SI")
chars_long = ("Sol Badguy", "Ky Kiske", "May", "Axl Low", "Chipp", "Potemkin", "Faust", "Millia", "Zato=1", "Ramlethal", "Leo Whitefang", "Nagoriyuki", "Anji Mito", "Ino", "Giovanna", "Jack-O", "Happy Chaos", "Baiken", "Testament", "Brisket", "Sin Kiske")
views = Blueprint(__name__, "views")

@views.route("/", methods=["GET", "POST"])
def home():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None 
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = []
    if request.method == "POST":
        floor = int(request.form["floor"])
        pick_rate_req = get_win_rates.get_pick_rates(floor)
    if request.method == "POST":
        floor = int(request.form["floor"])
        matchup_req = get_win_rates.get_matchups(floor)
        for matchup in matchup_req:
            if matchup == "-3":
                bad_matchups.append(matchup)
    return render_template("index.html", chars_long=chars_long, win_rate_req=win_rate_req, floor=floor, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/pickrate", methods=["GET", "POST"])
def pickrate():
    pick_rate_req = []
    if request.method == "POST":
        floor = int(request.form["floor"])
        pick_rate_req = get_win_rates.get_pick_rates(floor)
    return render_template("pickrate.html", pick_rate_req =pick_rate_req )

@views.route("/characters", methods=["GET", "POST"])
def characters():
    return render_template("characters.html")