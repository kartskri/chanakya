import json
import requests
import pandas as pd
from models.stock_model import Stock
from models.stock_model import Country


class stock_api:

    @staticmethod
    def stock_model(symbol):
        api_url = "http://52.206.118.2/eda/stock/" + symbol
        response = requests.get(api_url)
        # Parse API Response
        json_str = json.loads(response.text)
        # Stock From Dictionary
        m_stock = Stock.from_dict(json_str['stock'])
        # Income Reports
        m_income_reports_df = pd.DataFrame(json_str['incomeReports'])
        m_income_reports_df['fiscalDateEnding'] = m_income_reports_df['fiscalDateEnding'].astype('datetime64')
        # Stock Quotes
        m_quotes_df = pd.DataFrame(json_str['quotes'])
        # Return Stock, Income Statements, Quotes
        return m_stock, m_income_reports_df, m_quotes_df

    @staticmethod
    def macro_economic_data(country):
        api_url = "http://52.206.118.2/econ/country/" + country
        response = requests.get(api_url)
        # Parse API Response
        json_str = json.loads(response.text)
        # Country Meta Data
        country = Country.from_dict(json_str['country'])
        # Inflation Data
        inflation_yearly_df = pd.DataFrame.from_dict(data=[json_str['inflationYearly']]).T
        inflation_yearly_df.index = inflation_yearly_df.index.astype("uint64")
        inflation_yearly_df['year'] = inflation_yearly_df.index
        inflation_yearly_df.rename(columns={0: "percentages"}, inplace=True)
        inflation_yearly_df['percentages'] = inflation_yearly_df['percentages'].astype("double")
        # Return the Data frames
        return country, inflation_yearly_df
    

