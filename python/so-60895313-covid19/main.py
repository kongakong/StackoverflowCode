import pandas as pd
from pandas import DataFrame as df
import plotly.graph_objects as go
import requests
from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)

deaths_names = []

confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
yesterdays_date = yesterday.strftime('%-m/%d/%y')

confirmed = pd.read_csv(confirmed_url)
deaths = pd.read_csv(deaths_url, dtype={'Province/State': str})
confirmed.iloc[0]['Country/Region'] # Test


def fill_data(df):
    if df['Province/State'].str.count == 0:
        df['Name'] = df['Country/Region']
    else:
        df['Name'] = df['Province/State']


deaths.apply(fill_data, axis=1)

pd.set_option('display.max_rows', None)
print(deaths)
