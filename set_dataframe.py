import pandas as pd
import numpy as np

from get_data_from_web import list_making_for_column
from get_data_from_web_sise import high_low_price

def str_tidy(elem):
  elem = elem.replace(',', '')
  elem = elem.replace('\n', '')
  elem = elem.replace('\t', '')
  elem = elem.replace('%', '')
  return elem

def make_df():
  date, price, diff, diff_per, volume, gigwan, foreign = list_making_for_column()
  high_price, low_price = high_low_price()

  date = pd.Series(date)
  price = pd.Series(price)
  diff = pd.Series(diff)
  diff_per = pd.Series(diff_per)
  volume = pd.Series(volume)
  gigwan = pd.Series(gigwan)
  foreign = pd.Series(foreign)
  high_price = pd.Series(high_price)
  low_price = pd.Series(low_price)

  df = pd.DataFrame({"date":date, "price":price, "high_price":high_price, "low_price":low_price, "diff":diff, "diff_per":diff_per,
    "volume":volume, "gigwan":gigwan, "foreign":foreign})
  return df

def tidy_df():
  price_frame = make_df()
  price_frame['price'] = price_frame['price'].apply(str_tidy)
  price_frame['high_price'] = price_frame['high_price'].apply(str_tidy)
  price_frame['low_price'] = price_frame['low_price'].apply(str_tidy)
  price_frame['diff'] = price_frame['diff'].apply(str_tidy)
  price_frame['diff_per'] = price_frame['diff_per'].apply(str_tidy)
  price_frame['volume'] = price_frame['volume'].apply(str_tidy)
  price_frame['gigwan'] = price_frame['gigwan'].apply(str_tidy)
  price_frame['foreign'] = price_frame['foreign'].apply(str_tidy)
  price_frame.date = pd.to_datetime(price_frame.date, errors='coerce')
  price_frame.price = pd.to_numeric(price_frame.price, errors='coerce')
  price_frame.high_price = pd.to_numeric(price_frame.high_price, errors='coerce')
  price_frame.low_price = pd.to_numeric(price_frame.low_price, errors='coerce')
  price_frame.diff = pd.to_numeric(price_frame.diff, errors='coerce')
  price_frame.diff_per = pd.to_numeric(price_frame.diff_per, errors='coerce')
  price_frame.volume = pd.to_numeric(price_frame.volume, errors='coerce')
  price_frame.gigwan = pd.to_numeric(price_frame.gigwan, errors='coerce')
  price_frame.foreign = pd.to_numeric(price_frame.foreign, errors='coerce')
  return price_frame