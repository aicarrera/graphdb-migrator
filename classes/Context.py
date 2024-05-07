from Connection.APIconnection import *


class Context:

    def __init__(self, id_context, name="", value="", type=""):
        self.id = str(id_context)
        self.name = name
        self.value = value
        self.type = type



    def insert(self):
        print(vars(self))
        return insert_individuals(vars(self), "Context")

    def insertBatch(listObjects):
        json_individuals = [vars(ob) for ob in listObjects]
        return insert_batch_individuals(json_individuals, "Context")
