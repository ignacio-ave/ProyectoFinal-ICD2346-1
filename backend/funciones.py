import pandas as pd
from objetos import Candidato, Eleccion, EleccionPresidencial, EleccionSenadores

senadores_path = 'data/senadores_datos.csv'
presidenciales_path = 'data/presidentes_datos.csv'

senadores_df = pd.read_csv(senadores_path)
presidentes_df = pd.read_csv(presidenciales_path)


def eleccion_presidencial_con_votos_por_region(año):
    # Filtrar el DataFrame presidencial por el año dado
    presidenciales_año_df = presidentes_df[presidentes_df['Año de Elección'] == año]

    # Crear un objeto de elección presidencial
    fecha_eleccion = presidenciales_año_df['Fecha de Elección'].iloc[0].strftime('%d/%m/%Y')
    inicio_periodo = presidenciales_año_df['Inicio de Período'].iloc[0]
    fin_periodo = presidenciales_año_df['Fin de Período'].iloc[0]
    eleccion_presidencial = EleccionPresidencial(
        fecha=fecha_eleccion,
        año=año,
        cargo='PRESIDENTE',
        periodo_inicio=inicio_periodo,
        periodo_fin=fin_periodo,
        tipo='Presidencial'
    )

    # Agregar candidatos con votos por región al objeto de elección presidencial
    for candidato in presidenciales_año_df['Candidato (a)'].unique():
        votos_por_region = presidenciales_año_df[presidenciales_año_df['Candidato (a)'] == candidato]
        votos_por_region_dict = votos_por_region.set_index('Id Región')['Votos Totales'].to_dict()
        partido = votos_por_region['Partido'].iloc[0]
        eleccion_presidencial.agregar_candidato(
            nombre=candidato,
            partido=partido,
            votos_por_region=votos_por_region_dict
        )

    # Convertir el objeto de elección presidencial a un diccionario y retornarlo
    return eleccion_presidencial.to_dict()


# Función que procesa los datos de los senadores y crea un objeto de EleccionSenadores
def eleccion_senadores_con_votos_por_region(año):
    # Filtrar el DataFrame de senadores por el año dado
    senadores_año_df = senadores_df[senadores_df['Año de Elección'] == año]

    # Crear un objeto de elección de senadores
    fecha_eleccion = senadores_año_df['Fecha de Elección'].iloc[0]
    inicio_periodo = senadores_año_df['Inicio de Período'].iloc[0]
    fin_periodo = senadores_año_df['Fin de Período'].iloc[0]
    eleccion_senadores = EleccionSenadores(
        fecha=fecha_eleccion,
        año=año,
        cargo='SENADOR',
        periodo_inicio=inicio_periodo,
        periodo_fin=fin_periodo,
        tipo='Parlamentaria'
    )

    # Agregar candidatos con votos por región al objeto de elección de senadores
    for _, row in senadores_año_df.iterrows():
        votos_por_region = {row['Id Región']: row['Votos Totales']}
        electo = row['Electo(a)'] == 'SI'
        eleccion_senadores.agregar_candidato(
            nombre=row['Candidato (a)'],
            partido=row['Partido'],
            votos_por_region=votos_por_region,
            electo=electo
        )

    # Convertir el objeto de elección de senadores a un diccionario y retornarlo
    return eleccion_senadores.to_dict()
