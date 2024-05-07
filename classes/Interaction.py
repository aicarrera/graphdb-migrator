from Connection.APIconnection import *


class Interaction:

    def __init__(self, id_inter, id_sequence, element,order):
        self.id=id_inter
        self.idSequence=id_sequence
        self.element=element
        self.order=order

    def insertBatch(listInteractions):
        json_individuals = [vars(ob) for ob in listInteractions]
        return insert_batch_individuals(json_individuals,"Interaction")


  #  def __str__(self):
  #      return "{},{}".format(self.id,self.idSequence)
