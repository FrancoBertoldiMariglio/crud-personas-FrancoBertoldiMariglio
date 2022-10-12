import os
import json


class Persona:

    def __init__(self, documento, apellido, nombre):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre


class Diccionario:

    def __init__(self, person):
        self.diccionarioPersona = {
            "Documento": person.documento,
            "Apellido": person.apellido,
            "Nombre": person.nombre
        }


class PersonaService:

    def __init__(self):
        self.baseroot = str
        self.archivo = str

    def crearArchivo(self, archivo):
        self.baseroot = "G:\\Mi unidad\\Facultad\\Computación\\ArchivosPython\\Persona\\Archivos\\"
        self.archivo = self.baseroot + archivo
        file = open(self.archivo, "w")
        file.close

    def add(self, person):
        objDiccionario = Diccionario(person)
        file = open(self.archivo, "a")
        file.write(str(objDiccionario.diccionarioPersona) + os.linesep)
        file.close

    def delete(self, documento):
        file1 = open(self.archivo, 'r')
        lines = file1.readlines()
        file1.close()
        personaService = PersonaService()
        personaService.crearArchivo("person.txt")
        file2 = open(self.archivo, "a")
        for line in lines:
            line = line.replace("'", '"').replace("\n", "")
            if line != "":
                json_object = json.loads(line)
                if json_object["Documento"] != documento:
                    per = Persona(json_object["Documento"],
                                  json_object["Apellido"],
                                  json_object["Nombre"])
                    personaService.add(per)
        file2.close()

    def returnPersona(self, documento):
        file1 = open(self.archivo, 'r')
        lines = file1.readlines()
        for line in lines:
            line = line.replace("'", '"').replace("\n", "")
            if line != "":
                json_object = json.loads(line)
                if json_object["Documento"] == documento:
                    return json_object
        file1.close()
