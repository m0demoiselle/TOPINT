from models import db, Team, Event, Placement, User, Access
from application import app

app.app_context()

# Drop all then recreate all tables
db.drop_all()
db.create_all()

# adding unit information

db.session.add(Team(name="2-35 IN"))
db.session.add(Team(name="HHBN"))
db.session.add(Team(name="325 BSB"))
db.session.add(Team(name="2-25 AVN"))
db.session.add(Team(name="1-27 IN"))
db.session.add(Team(name="65 BEB"))
db.session.add(Team(name="3-7 FA"))
db.session.add(Team(name="2/14 CAV"))
db.session.add(Team(name="524 CSSB"))
db.session.add(Team(name="225 BSB"))
db.session.add(Team(name="3-25 AVN"))
db.session.add(Team(name="29 BEB"))
db.session.add(Team(name="2-11 FA"))
db.session.add(Team(name="1-21 IN"))
db.session.add(Team(name="2-6 CAV"))
db.session.add(Team(name="2-27 IN"))
db.session.add(Team(name="25th STB"))
db.session.add(Team(name="3/4 CAV"))
db.session.add(Team(name="209th ASB"))
db.session.commit()

# adding all event information
db.session.add(Event(id=0, name="Admin", weight=0))

db.session.add(Event(name="Softball Tournament", weight=6))
db.session.add(Event(name="Ultimate Frisbee", weight=6))
db.session.add(Event(name="Flag Football", weight=6))
db.session.add(Event(name="Tug-O-War", weight=6))
db.session.add(Event(name="Three-point contest", weight=6))
db.session.add(Event(name="Video Game Tourney", weight=6))
db.session.add(Event(name="Weight-Lifting / Strongman", weight=11))
db.session.add(Event(name="Combatives", weight=11))
db.session.add(Event(name="Swim Relay Competition", weight=6))
db.session.add(Event(name="Volleyball", weight=6))
db.session.add(Event(name="Bowling", weight=6))
db.session.add(Event(name="TL Got Talent", weight=6))
db.session.add(Event(name="Light Fighter Cook-Off", weight=6))
db.session.add(Event(name="10k Race", weight=11))
db.session.add(Event(name="Best Squad Competition", weight=11))
db.session.commit()

# adding all placement information
db.session.add(Placement(teams_id=1, events_id=1, place=8))
db.session.add(Placement(teams_id=2, events_id=1, place=14))
db.session.add(Placement(teams_id=3, events_id=1, place=5))
db.session.add(Placement(teams_id=4, events_id=1, place=6))
db.session.add(Placement(teams_id=5, events_id=1, place=10))
db.session.add(Placement(teams_id=6, events_id=1, place=13))
db.session.add(Placement(teams_id=7, events_id=1, place=16))
db.session.add(Placement(teams_id=8, events_id=1, place=1))
db.session.add(Placement(teams_id=9, events_id=1, place=18))
db.session.add(Placement(teams_id=10, events_id=1, place=12))
db.session.add(Placement(teams_id=11, events_id=1, place=3))
db.session.add(Placement(teams_id=12, events_id=1, place=7))
db.session.add(Placement(teams_id=13, events_id=1, place=15))
db.session.add(Placement(teams_id=14, events_id=1, place=4))
db.session.add(Placement(teams_id=15, events_id=1, place=11))
db.session.add(Placement(teams_id=16, events_id=1, place=19))
db.session.add(Placement(teams_id=17, events_id=1, place=2))
db.session.add(Placement(teams_id=18, events_id=1, place=17))
db.session.add(Placement(teams_id=19, events_id=1, place=9))

db.session.add(Placement(teams_id=1, events_id=2, place=5))
db.session.add(Placement(teams_id=2, events_id=2, place=14))
db.session.add(Placement(teams_id=3, events_id=2, place=12))
db.session.add(Placement(teams_id=4, events_id=2, place=2))
db.session.add(Placement(teams_id=5, events_id=2, place=19))
db.session.add(Placement(teams_id=6, events_id=2, place=15))
db.session.add(Placement(teams_id=7, events_id=2, place=6))
db.session.add(Placement(teams_id=8, events_id=2, place=17))
db.session.add(Placement(teams_id=9, events_id=2, place=7))
db.session.add(Placement(teams_id=10, events_id=2, place=16))
db.session.add(Placement(teams_id=11, events_id=2, place=11))
db.session.add(Placement(teams_id=12, events_id=2, place=1))
db.session.add(Placement(teams_id=13, events_id=2, place=3))
db.session.add(Placement(teams_id=14, events_id=2, place=13))
db.session.add(Placement(teams_id=15, events_id=2, place=9))
db.session.add(Placement(teams_id=16, events_id=2, place=4))
db.session.add(Placement(teams_id=17, events_id=2, place=18))
db.session.add(Placement(teams_id=18, events_id=2, place=10))
db.session.add(Placement(teams_id=19, events_id=2, place=8))

db.session.add(Placement(teams_id=1, events_id=3, place=17))
db.session.add(Placement(teams_id=2, events_id=3, place=9))
db.session.add(Placement(teams_id=3, events_id=3, place=18))
db.session.add(Placement(teams_id=4, events_id=3, place=11))
db.session.add(Placement(teams_id=5, events_id=3, place=14))
db.session.add(Placement(teams_id=6, events_id=3, place=10))
db.session.add(Placement(teams_id=7, events_id=3, place=5))
db.session.add(Placement(teams_id=8, events_id=3, place=6))
db.session.add(Placement(teams_id=9, events_id=3, place=7))
db.session.add(Placement(teams_id=10, events_id=3, place=2))
db.session.add(Placement(teams_id=11, events_id=3, place=8))
db.session.add(Placement(teams_id=12, events_id=3, place=3))
db.session.add(Placement(teams_id=13, events_id=3, place=13))
db.session.add(Placement(teams_id=14, events_id=3, place=15))
db.session.add(Placement(teams_id=15, events_id=3, place=16))
db.session.add(Placement(teams_id=16, events_id=3, place=19))
db.session.add(Placement(teams_id=17, events_id=3, place=1))
db.session.add(Placement(teams_id=18, events_id=3, place=4))
db.session.add(Placement(teams_id=19, events_id=3, place=12))

db.session.add(Placement(teams_id=1, events_id=4, place=4))
db.session.add(Placement(teams_id=2, events_id=4, place=15))
db.session.add(Placement(teams_id=3, events_id=4, place=5))
db.session.add(Placement(teams_id=4, events_id=4, place=11))
db.session.add(Placement(teams_id=5, events_id=4, place=12))
db.session.add(Placement(teams_id=6, events_id=4, place=9))
db.session.add(Placement(teams_id=7, events_id=4, place=13))
db.session.add(Placement(teams_id=8, events_id=4, place=17))
db.session.add(Placement(teams_id=9, events_id=4, place=18))
db.session.add(Placement(teams_id=10, events_id=4, place=2))
db.session.add(Placement(teams_id=11, events_id=4, place=7))
db.session.add(Placement(teams_id=12, events_id=4, place=3))
db.session.add(Placement(teams_id=13, events_id=4, place=19))
db.session.add(Placement(teams_id=14, events_id=4, place=10))
db.session.add(Placement(teams_id=15, events_id=4, place=1))
db.session.add(Placement(teams_id=16, events_id=4, place=6))
db.session.add(Placement(teams_id=17, events_id=4, place=16))
db.session.add(Placement(teams_id=18, events_id=4, place=8))
db.session.add(Placement(teams_id=19, events_id=4, place=14))

db.session.add(Placement(teams_id=1, events_id=5, place=2))
db.session.add(Placement(teams_id=2, events_id=5, place=1))
db.session.add(Placement(teams_id=3, events_id=5, place=9))
db.session.add(Placement(teams_id=4, events_id=5, place=15))
db.session.add(Placement(teams_id=5, events_id=5, place=10))
db.session.add(Placement(teams_id=6, events_id=5, place=12))
db.session.add(Placement(teams_id=7, events_id=5, place=19))
db.session.add(Placement(teams_id=8, events_id=5, place=16))
db.session.add(Placement(teams_id=9, events_id=5, place=11))
db.session.add(Placement(teams_id=10, events_id=5, place=18))
db.session.add(Placement(teams_id=11, events_id=5, place=13))
db.session.add(Placement(teams_id=12, events_id=5, place=8))
db.session.add(Placement(teams_id=13, events_id=5, place=17))
db.session.add(Placement(teams_id=14, events_id=5, place=14))
db.session.add(Placement(teams_id=15, events_id=5, place=4))
db.session.add(Placement(teams_id=16, events_id=5, place=5))
db.session.add(Placement(teams_id=17, events_id=5, place=3))
db.session.add(Placement(teams_id=18, events_id=5, place=6))
db.session.add(Placement(teams_id=19, events_id=5, place=7))

db.session.add(Placement(teams_id=1, events_id=6, place=12))
db.session.add(Placement(teams_id=2, events_id=6, place=9))
db.session.add(Placement(teams_id=3, events_id=6, place=14))
db.session.add(Placement(teams_id=4, events_id=6, place=18))
db.session.add(Placement(teams_id=5, events_id=6, place=5))
db.session.add(Placement(teams_id=6, events_id=6, place=7))
db.session.add(Placement(teams_id=7, events_id=6, place=19))
db.session.add(Placement(teams_id=8, events_id=6, place=11))
db.session.add(Placement(teams_id=9, events_id=6, place=3))
db.session.add(Placement(teams_id=10, events_id=6, place=4))
db.session.add(Placement(teams_id=11, events_id=6, place=15))
db.session.add(Placement(teams_id=12, events_id=6, place=8))
db.session.add(Placement(teams_id=13, events_id=6, place=16))
db.session.add(Placement(teams_id=14, events_id=6, place=13))
db.session.add(Placement(teams_id=15, events_id=6, place=2))
db.session.add(Placement(teams_id=16, events_id=6, place=6))
db.session.add(Placement(teams_id=17, events_id=6, place=17))
db.session.add(Placement(teams_id=18, events_id=6, place=10))
db.session.add(Placement(teams_id=19, events_id=6, place=1))

db.session.add(Placement(teams_id=1, events_id=7, place=10))
db.session.add(Placement(teams_id=2, events_id=7, place=4))
db.session.add(Placement(teams_id=3, events_id=7, place=7))
db.session.add(Placement(teams_id=4, events_id=7, place=3))
db.session.add(Placement(teams_id=5, events_id=7, place=14))
db.session.add(Placement(teams_id=6, events_id=7, place=16))
db.session.add(Placement(teams_id=7, events_id=7, place=9))
db.session.add(Placement(teams_id=8, events_id=7, place=2))
db.session.add(Placement(teams_id=9, events_id=7, place=15))
db.session.add(Placement(teams_id=10, events_id=7, place=19))
db.session.add(Placement(teams_id=11, events_id=7, place=11))
db.session.add(Placement(teams_id=12, events_id=7, place=6))
db.session.add(Placement(teams_id=13, events_id=7, place=17))
db.session.add(Placement(teams_id=14, events_id=7, place=8))
db.session.add(Placement(teams_id=15, events_id=7, place=5))
db.session.add(Placement(teams_id=16, events_id=7, place=1))
db.session.add(Placement(teams_id=17, events_id=7, place=18))
db.session.add(Placement(teams_id=18, events_id=7, place=12))
db.session.add(Placement(teams_id=19, events_id=7, place=13))

db.session.add(Placement(teams_id=1, events_id=8, place=11))
db.session.add(Placement(teams_id=2, events_id=8, place=6))
db.session.add(Placement(teams_id=3, events_id=8, place=16))
db.session.add(Placement(teams_id=4, events_id=8, place=12))
db.session.add(Placement(teams_id=5, events_id=8, place=14))
db.session.add(Placement(teams_id=6, events_id=8, place=1))
db.session.add(Placement(teams_id=7, events_id=8, place=18))
db.session.add(Placement(teams_id=8, events_id=8, place=9))
db.session.add(Placement(teams_id=9, events_id=8, place=10))
db.session.add(Placement(teams_id=10, events_id=8, place=7))
db.session.add(Placement(teams_id=11, events_id=8, place=3))
db.session.add(Placement(teams_id=12, events_id=8, place=13))
db.session.add(Placement(teams_id=13, events_id=8, place=19))
db.session.add(Placement(teams_id=14, events_id=8, place=15))
db.session.add(Placement(teams_id=15, events_id=8, place=5))
db.session.add(Placement(teams_id=16, events_id=8, place=17))
db.session.add(Placement(teams_id=17, events_id=8, place=8))
db.session.add(Placement(teams_id=18, events_id=8, place=2))
db.session.add(Placement(teams_id=19, events_id=8, place=4))

db.session.add(Placement(teams_id=1, events_id=9, place=2))
db.session.add(Placement(teams_id=2, events_id=9, place=1))
db.session.add(Placement(teams_id=3, events_id=9, place=13))
db.session.add(Placement(teams_id=4, events_id=9, place=9))
db.session.add(Placement(teams_id=5, events_id=9, place=4))
db.session.add(Placement(teams_id=6, events_id=9, place=11))
db.session.add(Placement(teams_id=7, events_id=9, place=7))
db.session.add(Placement(teams_id=8, events_id=9, place=10))
db.session.add(Placement(teams_id=9, events_id=9, place=19))
db.session.add(Placement(teams_id=10, events_id=9, place=6))
db.session.add(Placement(teams_id=11, events_id=9, place=14))
db.session.add(Placement(teams_id=12, events_id=9, place=3))
db.session.add(Placement(teams_id=13, events_id=9, place=16))
db.session.add(Placement(teams_id=14, events_id=9, place=8))
db.session.add(Placement(teams_id=15, events_id=9, place=17))
db.session.add(Placement(teams_id=16, events_id=9, place=5))
db.session.add(Placement(teams_id=17, events_id=9, place=12))
db.session.add(Placement(teams_id=18, events_id=9, place=18))
db.session.add(Placement(teams_id=19, events_id=9, place=15))

db.session.add(Placement(teams_id=1, events_id=10, place=9))
db.session.add(Placement(teams_id=2, events_id=10, place=8))
db.session.add(Placement(teams_id=3, events_id=10, place=4))
db.session.add(Placement(teams_id=4, events_id=10, place=16))
db.session.add(Placement(teams_id=5, events_id=10, place=5))
db.session.add(Placement(teams_id=6, events_id=10, place=3))
db.session.add(Placement(teams_id=7, events_id=10, place=13))
db.session.add(Placement(teams_id=8, events_id=10, place=14))
db.session.add(Placement(teams_id=9, events_id=10, place=18))
db.session.add(Placement(teams_id=10, events_id=10, place=17))
db.session.add(Placement(teams_id=11, events_id=10, place=10))
db.session.add(Placement(teams_id=12, events_id=10, place=19))
db.session.add(Placement(teams_id=13, events_id=10, place=7))
db.session.add(Placement(teams_id=14, events_id=10, place=12))
db.session.add(Placement(teams_id=15, events_id=10, place=11))
db.session.add(Placement(teams_id=16, events_id=10, place=6))
db.session.add(Placement(teams_id=17, events_id=10, place=2))
db.session.add(Placement(teams_id=18, events_id=10, place=15))
db.session.add(Placement(teams_id=19, events_id=10, place=1))

db.session.add(Placement(teams_id=1, events_id=11, place=3))
db.session.add(Placement(teams_id=2, events_id=11, place=1))
db.session.add(Placement(teams_id=3, events_id=11, place=7))
db.session.add(Placement(teams_id=4, events_id=11, place=5))
db.session.add(Placement(teams_id=5, events_id=11, place=13))
db.session.add(Placement(teams_id=6, events_id=11, place=4))
db.session.add(Placement(teams_id=7, events_id=11, place=2))
db.session.add(Placement(teams_id=8, events_id=11, place=11))
db.session.add(Placement(teams_id=9, events_id=11, place=9))
db.session.add(Placement(teams_id=10, events_id=11, place=12))
db.session.add(Placement(teams_id=11, events_id=11, place=17))
db.session.add(Placement(teams_id=12, events_id=11, place=14))
db.session.add(Placement(teams_id=13, events_id=11, place=10))
db.session.add(Placement(teams_id=14, events_id=11, place=19))
db.session.add(Placement(teams_id=15, events_id=11, place=16))
db.session.add(Placement(teams_id=16, events_id=11, place=6))
db.session.add(Placement(teams_id=17, events_id=11, place=18))
db.session.add(Placement(teams_id=18, events_id=11, place=15))
db.session.add(Placement(teams_id=19, events_id=11, place=8))

db.session.add(Placement(teams_id=1, events_id=12, place=5))
db.session.add(Placement(teams_id=2, events_id=12, place=7))
db.session.add(Placement(teams_id=3, events_id=12, place=8))
db.session.add(Placement(teams_id=4, events_id=12, place=2))
db.session.add(Placement(teams_id=5, events_id=12, place=4))
db.session.add(Placement(teams_id=6, events_id=12, place=16))
db.session.add(Placement(teams_id=7, events_id=12, place=12))
db.session.add(Placement(teams_id=8, events_id=12, place=15))
db.session.add(Placement(teams_id=9, events_id=12, place=18))
db.session.add(Placement(teams_id=10, events_id=12, place=10))
db.session.add(Placement(teams_id=11, events_id=12, place=11))
db.session.add(Placement(teams_id=12, events_id=12, place=3))
db.session.add(Placement(teams_id=13, events_id=12, place=17))
db.session.add(Placement(teams_id=14, events_id=12, place=13))
db.session.add(Placement(teams_id=15, events_id=12, place=1))
db.session.add(Placement(teams_id=16, events_id=12, place=14))
db.session.add(Placement(teams_id=17, events_id=12, place=9))
db.session.add(Placement(teams_id=18, events_id=12, place=19))
db.session.add(Placement(teams_id=19, events_id=12, place=6))

db.session.add(Placement(teams_id=1, events_id=13, place=4))
db.session.add(Placement(teams_id=2, events_id=13, place=15))
db.session.add(Placement(teams_id=3, events_id=13, place=3))
db.session.add(Placement(teams_id=4, events_id=13, place=17))
db.session.add(Placement(teams_id=5, events_id=13, place=14))
db.session.add(Placement(teams_id=6, events_id=13, place=18))
db.session.add(Placement(teams_id=7, events_id=13, place=16))
db.session.add(Placement(teams_id=8, events_id=13, place=12))
db.session.add(Placement(teams_id=9, events_id=13, place=19))
db.session.add(Placement(teams_id=10, events_id=13, place=1))
db.session.add(Placement(teams_id=11, events_id=13, place=13))
db.session.add(Placement(teams_id=12, events_id=13, place=9))
db.session.add(Placement(teams_id=13, events_id=13, place=8))
db.session.add(Placement(teams_id=14, events_id=13, place=7))
db.session.add(Placement(teams_id=15, events_id=13, place=11))
db.session.add(Placement(teams_id=16, events_id=13, place=6))
db.session.add(Placement(teams_id=17, events_id=13, place=10))
db.session.add(Placement(teams_id=18, events_id=13, place=5))
db.session.add(Placement(teams_id=19, events_id=13, place=2))

db.session.add(Placement(teams_id=1, events_id=14, place=6))
db.session.add(Placement(teams_id=2, events_id=14, place=1))
db.session.add(Placement(teams_id=3, events_id=14, place=8))
db.session.add(Placement(teams_id=4, events_id=14, place=13))
db.session.add(Placement(teams_id=5, events_id=14, place=4))
db.session.add(Placement(teams_id=6, events_id=14, place=11))
db.session.add(Placement(teams_id=7, events_id=14, place=14))
db.session.add(Placement(teams_id=8, events_id=14, place=5))
db.session.add(Placement(teams_id=9, events_id=14, place=2))
db.session.add(Placement(teams_id=10, events_id=14, place=15))
db.session.add(Placement(teams_id=11, events_id=14, place=19))
db.session.add(Placement(teams_id=12, events_id=14, place=16))
db.session.add(Placement(teams_id=13, events_id=14, place=3))
db.session.add(Placement(teams_id=14, events_id=14, place=10))
db.session.add(Placement(teams_id=15, events_id=14, place=18))
db.session.add(Placement(teams_id=16, events_id=14, place=17))
db.session.add(Placement(teams_id=17, events_id=14, place=7))
db.session.add(Placement(teams_id=18, events_id=14, place=9))
db.session.add(Placement(teams_id=19, events_id=14, place=12))

db.session.add(Placement(teams_id=1, events_id=15, place=0))
db.session.add(Placement(teams_id=2, events_id=15, place=0))
db.session.add(Placement(teams_id=3, events_id=15, place=0))
db.session.add(Placement(teams_id=4, events_id=15, place=0))
db.session.add(Placement(teams_id=5, events_id=15, place=0))
db.session.add(Placement(teams_id=6, events_id=15, place=0))
db.session.add(Placement(teams_id=7, events_id=15, place=0))
db.session.add(Placement(teams_id=8, events_id=15, place=0))
db.session.add(Placement(teams_id=9, events_id=15, place=0))
db.session.add(Placement(teams_id=10, events_id=15, place=0))
db.session.add(Placement(teams_id=11, events_id=15, place=0))
db.session.add(Placement(teams_id=12, events_id=15, place=0))
db.session.add(Placement(teams_id=13, events_id=15, place=0))
db.session.add(Placement(teams_id=14, events_id=15, place=0))
db.session.add(Placement(teams_id=15, events_id=15, place=0))
db.session.add(Placement(teams_id=16, events_id=15, place=0))
db.session.add(Placement(teams_id=17, events_id=15, place=0))
db.session.add(Placement(teams_id=18, events_id=15, place=0))
db.session.add(Placement(teams_id=19, events_id=15, place=0))

db.session.commit()

# creating user
db.session.add(User(code='WHO1ST'))
db.session.commit()

# create permissions for user
db.session.add(Access(user_id=1, event_id=0))
db.session.commit()

result = Team.query.all()

for r in result:
    team = Team.query.filter_by(id=r.id).first()
    team.update_score()
    print("--------------------")
db.session.commit()
