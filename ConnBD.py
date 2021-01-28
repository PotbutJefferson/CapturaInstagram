
import pymongo
from pymongo import MongoClient

class ConnBD:
  def __init__(self, host = "localhost", port = 27017, database = "ConectandoMongoDB", collection = "Usuarios"):
    self.host       = host
    self.port       = port
    self.database   = database
    self.collection = collection

  def getCollection(self):
    return self.collection

  def getDatabase(self):
    return self.database

  def conectar(self):
    self.conn = MongoClient(self.host, self.port).get_database(self.database).get_collection(self.collection)

  def insereRegistros(self, registers):
    self.conectar()
    self.conn.insert_many(registers)

  def consultaRegistros(self, condition):
    self.conectar()
    res = self.conn.find(condition)
    return res

  def consultaTodosRegistros(self):
    self.conectar()
    res = self.conn.find()
    return res

  def qtdeRegistros(self):
    self.conectar()
    res = self.conn.count()
    return res