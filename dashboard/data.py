import pandas as pd


df = pd.read_csv('output/all_traits_skills.csv', index_col=0)
df_occurrence = df[['relative_occurrence_job', 'total']]
