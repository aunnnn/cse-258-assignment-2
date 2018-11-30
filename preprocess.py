import pandas as pd
from pandas.api.types import CategoricalDtype

def __numerize_job_and_career_satisfaction(df):
  # Do it manually since we want to maintain the order/number. 
  career_satisfactions = [
    'Extremely dissatisfied',
    'Moderately dissatisfied',
    'Slightly dissatisfied',
    'Neither satisfied nor dissatisfied',
    'Slightly satisfied',
    'Moderately satisfied',
    'Extremely satisfied']

  cats = CategoricalDtype(categories=career_satisfactions, ordered=True)
  df['CareerSatisfaction'] = df['CareerSatisfaction'].astype(cats)
  df['CareerSatisfactionCode'] = df['CareerSatisfaction'].cat.codes - 3
  df['JobSatisfaction'] = df['JobSatisfaction'].astype(cats)
  df['JobSatisfactionCode'] = df['JobSatisfaction'].cat.codes - 3
  return df

def numerize_columns(df):
    __numerize_job_and_career_satisfaction(df)
    return df