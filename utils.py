import pandas as pd

# Load dataset
def load_dataset():
  df = pd.read_csv('./stack-overflow-2018-developer-survey/survey_results_public.tar.gz', low_memory=False)
  header = pd.read_csv('./stack-overflow-2018-developer-survey/survey_results_schema.csv', low_memory=False)

  # There's first weird column, so we remove it
  df = df.drop(df.columns[0], axis=1)
  return df, header

# View all possible values in a column.
# A list of checkbox options is separated with ';'
def get_unique_categories(df, column):
  return set([x for c in df[column].dropna().unique() for x in c.split(';')])

def get_column_of_interests():
  return [
    'Hobby', 
    'OpenSource', 
    'Country', 
    'Student',
    'Employment', 
    'FormalEducation', 
    'UndergradMajor', 
    'CompanySize',
    'DevType', 
    'YearsCoding', 
    'YearsCodingProf', 
    'JobSatisfaction',
    'CareerSatisfaction', 
    'JobSearchStatus',
    'LastNewJob',
    'Gender',
    'SexualOrientation',
    'Age'
  ]