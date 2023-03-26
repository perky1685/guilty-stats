from flask import render_template, Blueprint, request
import get_win_rates

views = Blueprint("views", __name__)

@views.route("/SO", methods=["GET", "POST"])
def SO():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/SO.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/KY", methods=["GET", "POST"])
def KY():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/KY.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/MA", methods=["GET", "POST"])
def MA():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/MA.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/AX", methods=["GET", "POST"])
def AX():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/AX.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/CH", methods=["GET", "POST"])
def CH():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/CH.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/PO", methods=["GET", "POST"])
def PO():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/PO.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/FA", methods=["GET", "POST"])
def FA():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/FA.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/MI", methods=["GET", "POST"])
def MI():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/MI.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/ZA", methods=["GET", "POST"])
def ZA():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/ZA.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/RA", methods=["GET", "POST"])
def RA():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/RA.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/LE", methods=["GET", "POST"])
def LE():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/LE.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/NA", methods=["GET", "POST"])
def NA():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/NA.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/GI", methods=["GET", "POST"])
def GI():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/GI.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/AN", methods=["GET", "POST"])
def AN():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/AN.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/IN", methods=["GET", "POST"])
def IN():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/IN.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/GO", methods=["GET", "POST"])
def GO():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/GO.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/JC", methods=["GET", "POST"])
def JC():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/JC.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/HA", methods=["GET", "POST"])
def HA():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/HA.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/BA", methods=["GET", "POST"])
def BA():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/BA.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/TE", methods=["GET", "POST"])
def TE():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/TE.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/BI", methods=["GET", "POST"])
def BI():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/BI.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

@views.route("/SI", methods=["GET", "POST"])
def SI():
    win_rate_req = []
    pick_rate_req = []
    matchup_req = []
    bad_matchups = []
    floor = None
    if request.method == "POST":
        floor = int(request.form["floor"])
        win_rate_req = get_win_rates.get_win_rates(floor)
        pick_rate_req = get_win_rates.get_pick_rates(floor)
        matchup_req = get_win_rates.get_matchups(floor)
    return render_template("character/SI.html", win_rate_req=win_rate_req, pick_rate_req=pick_rate_req, matchup_req=matchup_req, bad_matchups=bad_matchups)

