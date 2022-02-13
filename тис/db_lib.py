from sqlalchemy import create_engine, text


class MovieData(object):

    def __init__(self):
        self._engine = create_engine("sqlite:///db.db", echo = True)

    def get_movie(self):
        sql = text("SELECT Movie.id AS id, Movie.name as name, Movie.year"
                   "AS year, Movie.country AS countryFROM Movie")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_country(self, participant_id):
        sql = text("SELECT Participant.name AS Participant, Country.name "
                   "AS name FROM Participant JOIN CountryParticipant ON Participant.id ="
                   "CountryParticipant.participant_id JOIN Country ON CountryParticipant.participant_id = Country.id"
                   "WHERE Country.id in (SELECT CountryParticipant.country_id FROM CountryParticipant"
                   "WHERE CountryParticipant.participant_id=" + str(participant_id) + ") GROUP BY Country.id;")
        sql_result = self._engine.execute(sql)
        for record in sql_result:
            dictionary = dict(record)
        return dictionary["Country"]

    def get_participant_name(self, participant_id):
        sql = text("SELECT * FROM Participant WHERE id=" + str(participant_id) + ";")
        sql_result = self._engine.execute(sql)
        for auth in sql_result:
            res = str(auth["name"])
        return res

    def get_participant(self, participant_id):
        sql = text("SELECT GROUP_CONCAT(Participant.name,\", \") AS Participant, Movie.name "
                   "AS name, Movie.year AS year FROM Participant JOIN MovieParticipant ON Participant.id ="
                   "MovieParticipant.participant_id JOIN Movie ON MovieParticipant.participant_id = Movie.id"
                   "WHERE Movie.id in (SELECT MovieParticipant.movie_id FROM MovieParticipant"
                   "WHERE MovieParticipant.participant_id=" + str(participant_id) + ") GROUP BY Movie.id;")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_role_of_participant(self, participant_id):
        sql = text("SELECT Participant.name AS Participant, Role.name "
                   "AS name FROM Participant JOIN RoleParticipant ON Participant.id ="
                   "RoleParticipant.participant_id JOIN Role ON RoleParticipant.participant_id = Role.id"
                   "WHERE Role.id in (SELECT RoleParticipant.role_id FROM RoleParticipant"
                   "WHERE RoleParticipant.participant_id=" + str(participant_id) + ") GROUP BY Role.id;")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret


