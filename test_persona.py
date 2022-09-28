import unittest
import os
import json
from queue import Empty
from os.path import exists
from persona import Persona
from persona import Diccionario
from persona import PersonaService


class TestPersona(unittest.TestCase):

    def test_crear_persona(self):
        persona = Persona(44321123, "hongo", "pepito")
        self.assertEqual(persona.documento, 44321123)
        self.assertEqual(persona.apellido, "hongo")
        self.assertEqual(persona.nombre, "pepito")

    def test_crear_diccionario(self):
        persona = Persona(44321123, "hongo", "pepito")
        diccionariopersona = Diccionario(persona)
        self.assertEqual(
            diccionariopersona.diccionarioPersona, {
                "Documento": persona.documento,
                "Apellido": persona.apellido,
                "Nombre": persona.nombre
            })

    def test_crear_personaservice(self):
        personaservice = PersonaService()
        personaservice.crearArchivo("persona.txt")
        self.assertEqual(
            personaservice.baseroot,
            "G:\\Mi unidad\\Facultad\\Computación\\ArchivosPython\\Persona\\Archivos\\"
        )
        self.assertEqual(personaservice.archivo,
                         personaservice.baseroot + "persona.txt")

    def test_crear_archivo(self):
        personaservice = PersonaService()
        personaservice.crearArchivo("persona.txt")
        filepath = exists("persona.txt")
        self.assertTrue(filepath)

    def test_return_persona(self):
        persona = Persona(44321123, "pepito", "hongo")
        personaservice = PersonaService()
        personaservice.crearArchivo("persona.txt")
        personaservice.add(persona)
        personaEspecifica = personaservice.returnPersona(44321123)
        self.assertEqual(
            {
                "Documento": persona.documento,
                "Apellido": persona.apellido,
                "Nombre": persona.nombre
            }, personaEspecifica)


if __name__ == "__main__":
    unittest.main()
