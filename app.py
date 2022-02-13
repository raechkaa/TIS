from flask import Flask, render_template
from db_lib import MovieData


app = Flask(__name__)
bd = MovieData()


@app.route("/")
def movie():
    movies = bd.get_country_movie()
    ret = render_template("movie.html", movies=movies)
    return ret


@app.route("/m/<m_id>")
def participant(m_id=None):

    participant_role = bd.get_role_of_participant(m_id)
    ret = render_template("participant.html", participant_role=participant_role)
    return ret


@app.route("/m/participant/<participant_id>")
def information(participant_id=None):
    countries = bd.get_country(participant_id)
    participant_name = bd.get_participant_name(participant_id)
    participant_years = bd.get_participant(participant_id)
    ret = render_template("information.html", participant_years=participant_years, countries=countries, participant_name=participant_name)
    return ret


if __name__ == '__main__':
    app.debug = True
    app.run()

