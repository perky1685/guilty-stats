from flask import Blueprint, render_template, request
import get_win_rates
import os
from flask import render_template, request, send_file

chars_short = ("SO","KY","MA","AX","CH","PO","FA","MI","ZA","RA","LE","NA","GI","AN","IN","GO","JC","HA","BA","TE","BI","SI")
chars_long = ("Sol Badguy", "Ky Kiske", "May", "Axl Low", "Chipp", "Potemkin", "Faust", "Millia", "Zato=1", "Ramlethal", "Leo Whitefang", "Nagoriyuki", "Anji Mito", "Ino", "Giovanna", "Jack-O", "Happy Chaos", "Baiken", "Testament", "Brisket", "Sin Kiske")
views = Blueprint(__name__, "views")

@views.route("/", methods=["GET", "POST"])
def home():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = request.form.get("floor")  # get the value of the 'floor' field from the form, or None if it's not present
    if floor is not None:
        try:
            floor = int(floor)
        except ValueError:
            floor = None  # if the 'floor' value is not an integer, set it to None
    if request.method == "POST" and floor is not None:
        win_rate_req = get_win_rates.get_win_rates(floor)
    if request.method == "POST" and floor is not None:
        pick_rate_req = get_win_rates.get_pick_rates(floor)
    if request.method == "POST" and floor is not None:
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

from flask import render_template

@views.route("/characters", methods=["GET", "POST"])
def characters():
    image_path = ""
    matchup_req = []
    if request.method == 'POST':
        char = request.form['char']
        image_path = f"static/images/char/{char}.png"
    if request.method == 'POST':
        matchup_req = get_win_rates.get_all_matchups(char)
    return render_template("characters.html", image_path=image_path, matchup_req=matchup_req)

