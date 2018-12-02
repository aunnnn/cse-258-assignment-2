import pandas as pd
from pandas.api.types import CategoricalDtype
import preprocess

# Load orignal dataset
def load_dataset():
  df = pd.read_csv('./stack-overflow-2018-developer-survey/survey_results_public.tar.gz', low_memory=False)
  header = pd.read_csv('./stack-overflow-2018-developer-survey/survey_results_schema.csv', low_memory=False)

  # There's first weird column, so we remove it
  df = df.drop(df.columns[0], axis=1)

  return df, header

# Load dataset and preprocess
def load_dataset_processed():
  df, _ = load_dataset()

  # 1. Only columns we're interested
  df = df[Columns.all]

  # 2. Turn job satisfaction into ordered number from -3 to 3
  df = preprocess.numerize_job_satisfaction(df)

  df = preprocess.gender_with_only_male_female_others(df)

  # Turn categorical into its own columns
  df = preprocess.multilabel_encode(df, Columns.work + Columns.life + Columns.background)
  return df


# View all possible values in a series.
# A list of checkbox options is separated with ';'
def get_unique_categories(series):
  return set([x for c in series.dropna().unique() for x in c.split(';')])

# Columns that we're interested in
class Columns:

  for_prediction = [
    'JobSatisfaction', # cat, orderable
    'ConvertedSalary', # numerical
  ]
    
  work = [
    'CompanySize', # cat, orderable
    'DevType', # mult
    'LanguageWorkedWith', # mult
    'DatabaseWorkedWith', # mult
    'PlatformWorkedWith', # mult
    'OperatingSystem', # cat
  ]

  life = [
    'WakeTime', # cat, orderable
    'HoursComputer', # cat, orderable
    'HoursOutside', # cat, orderable
    'Hobby', # bool
    'SkipMeals', # cat
    'OpenSource', # bool
    'ErgonomicDevices', # mult
    'Exercise', # cat
  ]

  background = [
    'Country',
    'RaceEthnicity',
    'Gender', # male/female
    'Age', # cat, orderable
    'Student', # full/part/non
    'Employment', # cat
    'FormalEducation', # cat
    'UndergradMajor', # cat
    'YearsCoding', # cat, orderable
    'JobSearchStatus', # actively/not interested/not actively but open
    'LastNewJob', # 1-2 yrs/2-4 yrs/etc.
    'EducationTypes', # cat
    'EducationParents',
  ]

  all = for_prediction + background + work + life

# Print what's that column is all about from header
def describe_column(header, name):
  return header[header['Column'] == name]['QuestionText'].values[0]
