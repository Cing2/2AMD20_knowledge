import pandas as pd

df = pd.read_csv('output/all_traits_skills.csv', index_col=0)
df_occurrence = df[['relative_occurrence_job', 'total']]

df_all_job = pd.read_csv('output/all_jobdescriptions.csv')


def get_word_count_jobs(word_to_search: str) -> int:
    word_to_search = word_to_search.lower()
    df_all_job['count_word'] = df_all_job['job_description'].apply(lambda x: x.count(word_to_search))
    sum_word = df_all_job['count_word'].sum()

    return sum_word
