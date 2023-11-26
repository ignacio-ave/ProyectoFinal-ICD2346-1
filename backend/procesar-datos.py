import pandas as pd

# Rutas de los archivos
presidenciales_path = 'data/resultados_elecciones_presidenciales_ce_1989_2017_Chile.xlsx'

# Cargar los datos
presidentes_df = pd.read_excel(presidenciales_path)

# Columnas a conservar
columns_to_keep = [
    "Tipo de Elección", "Cargo", "Fecha de Elección", "Año de Elección", 
    "Inicio de Período", "Fin de Período", "Id Región", "Región", "Provincia", 
    "Nombre Provincia", "Comuna", "Candidato (a)", "Electo(a)", "Partido", 
    "Sigla Partido", "Votos Totales", "Votación Presidencial"
]

# Filtrar las columnas
presidentes_df_simplified = presidentes_df[columns_to_keep]

# Función para limpiar votos
def clean_votes(votes):
    if isinstance(votes, str):
        return int(votes.replace(',', '').replace('.', ''))
    return votes

# Limpiar columna de votos usando .loc para evitar el warning
presidentes_df_simplified.loc[:, 'Votos Totales'] = presidentes_df_simplified['Votos Totales'].apply(clean_votes)

# Crear MultiIndex incluyendo el tipo de votación
presidentes_df_multiindex = presidentes_df_simplified.set_index([
    "Año de Elección", "Votación Presidencial", "Candidato (a)", "Región", "Provincia", "Comuna"
])

# Definir funciones de agregación
agg_funcs = {col: 'first' for col in presidentes_df_multiindex.columns.difference(['Votos Totales'])}
agg_funcs['Votos Totales'] = 'sum'

# Agrupar datos
presidentes_df_grouped = presidentes_df_multiindex.groupby(level=["Año de Elección", "Votación Presidencial", "Candidato (a)", "Región", "Provincia"]).agg(agg_funcs)

# Restablecer índice
presidentes_df_grouped_reset = presidentes_df_grouped.reset_index()

# Ordenar datos
presidentes_df_sorted = presidentes_df_grouped_reset.sort_values(
    by=['Fecha de Elección', 'Votación Presidencial', 'Id Región', 'Provincia', 'Votos Totales'],
    ascending=[True, True, True, True, False]
)

# Guardar los DataFrames como CSV
presidentes_df_sorted.to_csv('data/presidentes_datos.csv', index=False)
