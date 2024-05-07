from Connection.APIconnection import *


class Service:

    def __init__(self, id_service, name, location, services):
        self.id = id_service
        self.name = name
        self.location= location
        self.services = services
    def insert(self):
        return request_template("http://userinteraction_context/service_insert", vars(self))




    def insertBatch(listObjects):
        json_individuals = [vars(ob) for ob in listObjects]
        print("-",json_individuals)
        return insert_batch_individuals(json_individuals, "Service")