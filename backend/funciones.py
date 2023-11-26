import pandas as pd
import numpy as np
from objetos import Candidato, Eleccion, EleccionPresidencial, EleccionSenadores

#senadores_path = 'backend/data/senadores_datos.csv'
presidenciales_path = '/workspaces/ProyectoFinal-ICD2346-1/backend/data/presidentes_datos.csv'

# senadores_df = pd.read_csv(senadores_path)
presidentes_df = pd.read_csv(presidenciales_path)

def convert_int64(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = convert_int64(value)
    elif isinstance(obj, list):
        return [convert_int64(item) for item in obj]
    elif isinstance(obj, (np.int64, np.int32)):
        return int(obj)
    return obj


def eleccion_presidencial_con_votos_por_region(año):
    # Primero intentar con "VOTACIÓN ÚNICA"
    filtro_unico = (presidentes_df['Año de Elección'] == año) & (presidentes_df['Votación Presidencial'] == "ÚNICA VOTACIÓN")
    presidenciales_año_df = presidentes_df[filtro_unico]

    # Si no hay datos para "VOTACIÓN ÚNICA", intentar con "PRIMERA VOTACIÓN"
    if presidenciales_año_df.empty:
        filtro_primera = (presidentes_df['Año de Elección'] == año) & (presidentes_df['Votación Presidencial'] == "PRIMERA VOTACIÓN")
        presidenciales_año_df = presidentes_df[filtro_primera]

        # Si tampoco hay datos para "PRIMERA VOTACIÓN", devolver un error
        if presidenciales_año_df.empty:
            return {'error': f'No hay datos disponibles para el año {año}'}

    # Corrección aquí: eliminar strftime
    fecha_eleccion = presidenciales_año_df['Fecha de Elección'].iloc[0]
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

    resultado_dict = eleccion_presidencial.to_dict()
    resultado_convertido = convert_int64(resultado_dict)
    return resultado_convertido

def hay_segunda_instancia(año):
    filtro_segunda = (presidentes_df['Año de Elección'] == año) & (presidentes_df['Votación Presidencial'] == "SEGUNDA VOTACIÓN")
    return not presidentes_df[filtro_segunda].empty

def resultados_presidenciales_por_region_provincia(año):
    resultados_finales = []
    for instancia in ["ÚNICA VOTACIÓN", "PRIMERA VOTACIÓN", "SEGUNDA VOTACIÓN"]:
        filtro = (presidentes_df['Año de Elección'] == año) & (presidentes_df['Votación Presidencial'] == instancia)
        df_filtrado = presidentes_df[filtro]

        if not df_filtrado.empty:
            # Agrupar por región y provincia, sumando los votos
            resultados = df_filtrado.groupby(['Región', 'Provincia', 'Candidato (a)']).agg({'Votos Totales': 'sum'}).reset_index().to_dict(orient='records')
            resultados_finales.append({"instancia": instancia, "resultados": resultados})

    if not resultados_finales:
        return {'error': f'No hay datos disponibles para el año {año}.'}

    return resultados_finales

def resultados_presidenciales_por_region_especifica(año, region, instancia_votacion=None):
    if instancia_votacion is None:
        for instancia in ["ÚNICA VOTACIÓN", "PRIMERA VOTACIÓN"]:
            filtro = (presidentes_df['Año de Elección'] == año) & (presidentes_df['Votación Presidencial'] == instancia) & (presidentes_df['Región'] == region)
            df_filtrado = presidentes_df[filtro]
            if not df_filtrado.empty:
                break
    else:
        filtro = (presidentes_df['Año de Elección'] == año) & (presidentes_df['Votación Presidencial'] == instancia_votacion) & (presidentes_df['Región'] == region)
        df_filtrado = presidentes_df[filtro]

    if df_filtrado.empty:
        return {'error': f'No hay datos disponibles para el año {año}, región {region} y la instancia de votación especificada.'}

    resultados = df_filtrado.groupby(['Provincia', 'Candidato (a)']).agg({'Votos Totales': 'sum'}).reset_index().to_dict(orient='records')
    return resultados


# Función que procesa los datos de los senadores y crea un objeto de EleccionSenadores

def eleccion_senadores_con_votos_por_region(año):
    # Filtrar el DataFrame de senadores por el año dado
    senadores_año_df = senadores_df[senadores_df['Año de Elección'] == año]

    # Verificar si hay datos para el año especificado
    if senadores_año_df.empty:
        return {'error': f'No hay datos disponibles para el año {año}'}

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


    resultado_dict = eleccion_senadores.to_dict()
    resultado_convertido = convert_int64(resultado_dict)
    return resultado_convertido

