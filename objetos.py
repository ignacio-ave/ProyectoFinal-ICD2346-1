import pandas as pd


# Definición de clases
class Candidato:
    def __init__(self, nombre, partido, votos_por_region, electo=None):
        self.nombre = nombre
        self.partido = partido
        self.votos_por_region = votos_por_region
        self.electo = electo


    def votos_totales(self):
        return sum(self.votos_por_region.values())

    def to_dict(self):
        # Ordenar los votos por región según el ID de la región
        votos_ordenados_por_region = dict(sorted(self.votos_por_region.items()))
        return {
            'nombre': self.nombre,
            'partido': self.partido,
            'votos_por_region': votos_ordenados_por_region,
            'votos_totales': self.votos_totales(),
            'electo': self.electo

        }

class Eleccion:
    def __init__(self, fecha, año, cargo, periodo_inicio, periodo_fin, tipo):
        self.fecha = fecha
        self.año = año
        self.cargo = cargo
        self.periodo_inicio = periodo_inicio
        self.periodo_fin = periodo_fin
        self.tipo = tipo
        self.candidatos = []

    def agregar_candidato(self, nombre, partido, votos_por_region, electo=None):
        candidato = Candidato(nombre, partido, votos_por_region, electo)
        self.candidatos.append(candidato)

    def to_dict(self):
        return {
            'fecha': self.fecha,
            'año': self.año,
            'cargo': self.cargo,
            'periodo_inicio': self.periodo_inicio,
            'periodo_fin': self.periodo_fin,
            'tipo': self.tipo,
            'candidatos': [candidato.to_dict() for candidato in self.candidatos]
        }

class EleccionPresidencial(Eleccion):
    def __init__(self, fecha, año, cargo, periodo_inicio, periodo_fin, tipo):
        super().__init__(fecha, año, cargo, periodo_inicio, periodo_fin, tipo)
        self.votos_totales_nacionales = 0

    def agregar_candidato(self, nombre, partido, votos_por_region):
        # Agregar los votos totales por región al total nacional
        self.votos_totales_nacionales += sum(votos_por_region.values())
        super().agregar_candidato(nombre, partido, votos_por_region)

    def to_dict(self):
        # Incluir la votación total nacional en la representación del diccionario
        eleccion_dict = super().to_dict()
        eleccion_dict['votos_totales_nacionales'] = self.votos_totales_nacionales
        return eleccion_dict

# Clase para elecciones de senadores

class EleccionSenadores(Eleccion):

    def to_dict(self):
        eleccion_dict = super().to_dict()
        return eleccion_dict

