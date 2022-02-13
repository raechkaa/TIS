from sqlalchemy import create_engine, text


class MovieData(object):

    def __init__(self):
        self._engine = create_engine("sqlite:///db.db", echo=True)

    def get_country(self, participant_id):
        sql = text("SELECT "
                   " group_concat(Country.name, ', ') as country"
                   " FROM Participant JOIN CountryParticipant ON Participant.id ="
                   " CountryParticipant.participant_id join Country on CountryParticipant.country_id = Country.id"
                   " WHERE Participant.id in"
                   " (SELECT CountryParticipant.participant_id "
                   " FROM CountryParticipant WHERE CountryParticipant.participant_id=" +
                   str(participant_id) + ")"
                   " group by Participant.id")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_participant_name(self, participant_id):
        sql = text("SELECT Participant.name as name FROM Participant"
                   " WHERE Participant.id in"
                   " (SELECT Participant.id FROM Participant WHERE Participant.id=" +
                   str(participant_id) + ")"
                   " group by Participant.id")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))

        return ret

    def get_participant(self, participant_id):
        sql = text("select Participant.birth_year as birth_year, "
                   " case "
                   " when Death.year is Null then 'ныне живущий'"
                   " else Death.year"
                   "  end as year_of_life"
                   " from Participant left join Death "
                   "  on Participant.id = Death.participant_id"
                   " WHERE Participant.id in"
                   " (SELECT Participant.id FROM Participant WHERE Participant.id=" +
                   str(participant_id) + ")"
                   " group by Participant.id")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_role_of_participant(self, m_id):
        sql = text("SELECT Participant.name, Participant.id as id, group_concat(Role.name, ', ') as role FROM Role"
                   " join MovieRoleParticipant on MovieRoleParticipant.role_id = Role.id join Participant"
                   " on Participant.id = MovieRoleParticipant.participant_id "
                   " join Movie on MovieRoleParticipant.movie_id = Movie.id"
                   " WHERE Movie.id in"
                   " (SELECT MovieRoleParticipant.movie_id FROM MovieRoleParticipant "
                   "WHERE MovieRoleParticipant.movie_id=" +
                   str(m_id) + ")"
                   " group by Participant.id")

        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_country_movie(self):
        sql = text("SELECT Movie.id as id, Movie.name as name, Movie.year as year,"
                   " group_concat(Country.name, ', ') as country"
                   " FROM Movie JOIN CountryMovie ON Movie.id ="
                   " CountryMovie.movie_id join Country on CountryMovie.country_id = Country.id"
                   " group by movie.id")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

