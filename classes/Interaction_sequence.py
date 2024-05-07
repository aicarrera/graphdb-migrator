
from Connection.APIconnection import *


class InteractionSequence:

    def __init__(self, id_sequence, start_date,end_date, id_user, id_subservice, contexts,value):
        self.id = id_sequence
        self.startDate = start_date
        self.endDate = end_date
        self.idUser = id_user
        self.idSubservice = id_subservice
        self.contexts=contexts
        self.value=value

    def insert(self):
        return insert_individuals(vars(self),"InteractionSequence")

    def insertBatch(listInteractions):
        json_individuals = [vars(ob) for ob in listInteractions]
        return insert_batch_individuals(json_individuals,"InteractionSequence")