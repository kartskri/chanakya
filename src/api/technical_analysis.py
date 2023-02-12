import pandas_ta as pta

class TechnicalAnalysis:

    @staticmethod
    def moving_averages(df):
        temp_stock_moving_averages = df[['date', 'symbol', 'adjustedClose']]
        temp_stock_moving_averages['year'] = temp_stock_moving_averages['date'].dt.year
        # Simple Moving Averages
        temp_stock_moving_averages['sma_20'] = temp_stock_moving_averages['adjustedClose'].rolling(20).mean()
        temp_stock_moving_averages['sma_200'] = temp_stock_moving_averages['adjustedClose'].rolling(200).mean()
        # Exponential Moving Averages
        temp_stock_moving_averages['ema_20'] = temp_stock_moving_averages['adjustedClose'].ewm(20).mean()
        temp_stock_moving_averages['ema_200'] = temp_stock_moving_averages['adjustedClose'].ewm(200).mean()
        # Cumulative Sum Moving Averages
        temp_stock_moving_averages['cum_ma'] = temp_stock_moving_averages['adjustedClose'].expanding().mean()
        # Dataframe Quotes
        temp_stock_moving_averages.dropna(inplace=True)
        return temp_stock_moving_averages

    @staticmethod
    def bollinger_bands(temp_bbands):
        temp_bbands['year'] = temp_bbands['date'].dt.year
        temp_bbands['standard_dev'] = temp_bbands['adjustedClose'].rolling(20).std(ddof=0)
        temp_bbands['sma_20'] = temp_bbands['adjustedClose'].rolling(20).mean()
        temp_bbands['bollinger_upper'] = temp_bbands['sma_20'] + 2 * temp_bbands['standard_dev']
        temp_bbands['bollinger_lower'] = temp_bbands['sma_20'] - 2 * temp_bbands['standard_dev']
        temp_bbands.dropna(inplace=True)
        return temp_bbands


    @staticmethod
    def rsi_calc(temp_rsi_calc):
        # Compute RSI
        temp_rsi_calc['rsi'] = pta.rsi(temp_rsi_calc['adjustedClose'], timeperiod=14)
        temp_rsi_calc.dropna(inplace=True)
        return temp_rsi_calc

 