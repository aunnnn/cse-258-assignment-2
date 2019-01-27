import pandas as pd
from pandas.api.types import CategoricalDtype
from sklearn.preprocessing import MultiLabelBinarizer

satisfactions = [
    'Extremely dissatisfied',
    'Moderately dissatisfied',
    'Slightly dissatisfied',
    'Neither satisfied nor dissatisfied',
    'Slightly satisfied',
    'Moderately satisfied',
    'Extremely satisfied']

# Starting with 0
def numerize_column_with_orders(df, col, orders):
  # Do it manually since we want to maintain the order/number. 
  cats = CategoricalDtype(categories=orders, ordered=True)
  df = df.copy()
  df[col] = df[col].astype(cats)
  # df[col] = df[col].cat.codes
  # df['JobSatisfactionCode'] = df['JobSatisfaction'].cat.codes - 3
  return df

# Turn job satisfaction into number [-3 to 3] (From dissatisfied to satisfied)
def numerize_job_satisfaction(df):
  # Do it manually since we want to maintain the order/number. 
  cats = CategoricalDtype(categories=satisfactions, ordered=True)
  df['JobSatisfaction'] = df['JobSatisfaction'].astype(cats)
  df['JobSatisfaction'] = df['JobSatisfaction'].cat.codes - 3
  # df['JobSatisfactionCode'] = df['JobSatisfaction'].cat.codes - 3
  return df

def gender_with_only_male_female_others(df):
  gender = df['Gender']
  gender[~((gender == 'Male') | (gender == 'Female'))] = 'Others'
  df['Gender'] = gender
  return df

def multilabel_encode(df, cols, fill_na_with='Unknown'):
  mlb = MultiLabelBinarizer()  
  encoded = [pd.DataFrame(mlb.fit_transform(df[col].fillna(fill_na_with).str.split(';')), columns=mlb.classes_).add_prefix(col + "_") for col in cols]
  # Drop original columns 
  return df.drop(columns=cols).join(encoded)
