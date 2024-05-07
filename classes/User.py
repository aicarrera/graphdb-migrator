from Connection.APIconnection import *


class User:

    def __init__(self, id_user, name):
        self.id = str(id_user)
        self.name = name

    def insert(self):
        return request_template("http://userinteraction_context/user_insert", vars(self))


    def insertBatch(listObjects):
        json_individuals = [vars(ob) for ob in listObjects]
        return insert_batch_individuals(json_individuals, "User")