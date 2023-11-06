import pandas as pd

senadores_path = 'data/resultados_elecciones_senadores_ce_1989_2017.xlsx'
presidenciales_path = 'data/resultados_elecciones_presidenciales_ce_1989_2017_Chile.xlsx'

senadores_df = pd.read_excel(senadores_path)
presidentes_df = pd.read_excel(presidenciales_path)


columns_to_keep = [
    "Tipo de Elección", "Cargo", "Fecha de Elección", "Año de Elección", 
    "Inicio de Período", "Fin de Período", "Id Región", "Región", "Comuna", 
    "Candidato (a)", "Electo(a)", "Partido", "Sigla Partido", "Votos Totales"
]

senadores_df_simplified = senadores_df[columns_to_keep]
presidentes_df_simplified = presidentes_df[columns_to_keep]

def clean_votes(votes):
    if isinstance(votes, str):
        return int(votes.replace(',', '').replace('.', ''))
    return votes

senadores_df_simplified['Votos Totales'] = senadores_df_simplified['Votos Totales'].apply(clean_votes)
presidentes_df_simplified['Votos Totales'] = presidentes_df_simplified['Votos Totales'].apply(clean_votes)

senadores_df_multiindex = senadores_df_simplified.set_index([
    "Año de Elección", "Candidato (a)", "Región", "Comuna"
])

presidentes_df_multiindex = presidentes_df_simplified.set_index([
    "Año de Elección", "Candidato (a)", "Región", "Comuna"
])

agg_funcs = {col: 'first' for col in senadores_df_multiindex.columns.difference(['Votos Totales'])}
agg_funcs['Votos Totales'] = 'sum'

senadores_df_grouped = senadores_df_multiindex.groupby(level=["Año de Elección", "Candidato (a)", "Región"]).agg(agg_funcs)
presidentes_df_grouped = presidentes_df_multiindex.groupby(level=["Año de Elección", "Candidato (a)", "Región"]).agg(agg_funcs)

senadores_df_grouped['Votacion Total'] = senadores_df_grouped.groupby(level=["Año de Elección", "Candidato (a)"])['Votos Totales'].transform('sum')
presidentes_df_grouped['Votacion Total'] = presidentes_df_grouped.groupby(level=["Año de Elección", "Candidato (a)"])['Votos Totales'].transform('sum')

senadores_df_grouped_reset = senadores_df_grouped.reset_index()
presidentes_df_grouped_reset = presidentes_df_grouped.reset_index()

senadores_df_grouped_reset = senadores_df_grouped.reset_index()
presidentes_df_grouped_reset = presidentes_df_grouped.reset_index()

senadores_df_grouped_reset['Electo_Sort'] = senadores_df_grouped_reset['Electo(a)'].apply(lambda x: 1 if x == 'SI' else 0)
presidentes_df_grouped_reset['Electo_Sort'] = presidentes_df_grouped_reset['Electo(a)'].apply(lambda x: 1 if x == 'SI' else 0)

senadores_df_sorted = senadores_df_grouped_reset.sort_values(
    by=['Fecha de Elección', 'Id Región', 'Electo_Sort', 'Votos Totales'],
    ascending=[True, True, False, False]
)

presidentes_df_sorted = presidentes_df_grouped_reset.sort_values(
    by=['Fecha de Elección', 'Id Región', 'Electo_Sort', 'Votos Totales'],
    ascending=[True, True, False, False]
)

senadores_df_sorted.drop('Electo_Sort', axis=1, inplace=True)
presidentes_df_sorted.drop('Electo_Sort', axis=1, inplace=True)

# Guardar los DataFrames como CSV
senadores_df_sorted.to_csv('data/senadores_datos.csv', index=False)
presidentes_df_sorted.to_csv('data/presidentes_datos.csv', index=False)
