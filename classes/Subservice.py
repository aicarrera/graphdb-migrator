from Connection.APIconnection import *

class Subservice:

    def __init__(self, id_subservice, name):
        self.id = id_subservice
        self.name = name

    def insert(self):
        return request_template("http://userinteraction_context/subservice_insert", vars(self))

    def insertBatch(listObjects):
        json_individuals = [vars(ob) for ob in listObjects]
        return insert_batch_individuals(json_individuals, "Subservice")