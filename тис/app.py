from flask import Flask, render_template
from db_lib import MovieData


app = Flask(__name__)
bd = MovieData()


@app.route("/")
def movie():
    movie_list = bd.get_movie()
    ret = render_template("movie.html", movie_list=movie_list)
    return ret


@app.route("/participant/<participant_id>")
def participant(participant_id=None):
    participant_list = bd.get_participant_name(participant_id)
    participant_role = bd.get_role_of_participant(participant_id)
    ret = render_template("participant.html", participant_list=participant_list, participant_role=participant_role)
    return ret


@app.route("/info")
def info(participant_id=None):
    participant_name = bd.get_participant_name(participant_id)
    participant_country = bd.get_country(participant_id)
    participant_death = bd.get_participant(participant_id)
    ret = render_template("participant.html", participant_name=participant_name,
                          participant_country=participant_country, participant_death=participant_death)
    return ret



if __name__ == '__main__':
    app.debug = True
    app.run()

