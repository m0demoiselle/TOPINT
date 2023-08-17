import flask
from flask import url_for  # imported for use in frontend
from flask_debugtoolbar import DebugToolbarExtension

from env import DB_URI, FLASK_SECRETKEY
import models
from ordinalize import num_to_ordinal

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config["SECRET_KEY"] = FLASK_SECRETKEY
debug = DebugToolbarExtension(app)

models.connect_db(app)
app.app_context().push()
models.db.create_all()


@app.route('/')
def home():
    teams = models.Team.query.all()  # create a list of teams participating
    for t in teams:
        t.update_score()

    teams = models.Team.query.order_by(-models.Team.score).all()  # list of teams, ordered by score (desc)
    events = models.Event.query.order_by(models.Event.id).all()  # list of all events, ordered by id

    # create header for scoreboard table
    header = ["Teams"]
    for e in events:
        header.append(e.name)
    header.append("Total Score")

    scoreboard = [header]  # create scoreboard table with header row

    for team in teams:
        # loop generates a row with team name and scores from each event
        row = [team.name]  # generate a row with team name as first item

        # query with all the team's placements, ordered by event id
        placements = models.Placement.query.filter_by(teams_id=team.id).order_by(models.Placement.events_id)
        for placement in placements:
            if placement.place == 0:
                row.append("N/A")
            else:
                row.append(models.place_to_score(placement.place) *  # raw score from placement
                           models.Event.query.filter_by(id=placement.events_id).first().weight)  # weight from event

        row.append(team.score)
        scoreboard.append(row)

    return flask.render_template('index.html', teams=teams, scoreboard=scoreboard)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if flask.request.method == 'POST':  # called when login button redirects to login()
        password = flask.request.form['password'].upper()
        query = models.User.query.filter_by(code=password)

        if query.count() == 0:  # no match found, send back to login()
            print("Code '{}' not found".format(password))
            flask.flash("Error! Incorrect code presented.", "danger")
            return flask.redirect(flask.url_for('login'))

        else:  # match found, send to edit()
            query = models.User.query.filter_by(code=password)
            flask.session['event_id'] = query.first().events_id
            flask.flash("Login successful!", "success")
            return flask.redirect(flask.url_for('edit'))

    return flask.render_template('login.html')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    # TODO: pre-select placement for each team based on previous data entry
    event_id = flask.session['event_id']
    event = models.Event.query.filter_by(id=event_id).first()
    teams = models.Team.query.order_by(models.Team.id)
    placements = []
    for i in range(teams.count()):
        placements.append((i + 1, num_to_ordinal(i + 1)))
    return flask.render_template('edit.html', event=event, teams=teams, placements=placements)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if flask.request.method == 'POST':
        db_submit = {}  # list to be stored in session
        for item in flask.request.form:
            key = convert_to_id(item)  # receiving team id as integer
            value = convert_to_id(flask.request.form[item])  # receiving team placement as integer
            db_submit[key] = value
        flask.session['db_submit'] = db_submit  # loaded into submit for future feature (confirmation page)

        # this loops through all the submission and updates record
        event_id = flask.session['event_id']
        for team_id in db_submit:
            placement = models.Placement.query.get((team_id, event_id))
            placement.place = db_submit[team_id]
            models.db.session.commit()

        flask.flash("Submit successful!", "success")
    else:
        flask.flash("Unknown error encountered.", "danger")
    return flask.render_template('submit.html')


def convert_to_id(string):
    if string.startswith("teamid_"):
        return int(string.split("_")[1])
    if string.isnumeric:
        return int(string)


if __name__ == '__main__':
    app.run(debug=True)
