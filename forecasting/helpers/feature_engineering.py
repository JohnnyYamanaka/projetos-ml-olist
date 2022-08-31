import pandas as pd

class FeatureEngineering():
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def is_holiday(self, holiday: list):
        df = self.dataframe
        df['is_holiday'] = df['day_of_purchase'].apply(
            lambda x: 1 if x in holiday else 0
        )

    def is_commercial_day(self, list_date):
        df = self.dataframe
        df['is_commercial_day'] = df['day_of_purchase'].apply(
            lambda x: 1 if x in list_date else 0
        )

    def day_of_week(self):
        df = self.dataframe
        df['day_of_week'] = df['day_of_purchase'].dt.weekday
        
    def day_of_month(self):
        df = self.dataframe
        df['day_of_month'] = df['day_of_purchase'].dt.day

    def day_of_year(self):
        df = self.dataframe
        df['day_of_year'] = df['day_of_purchase'].dt.dayofyear

    def moving_average(self):
        df = self.dataframe
        df['ma_7'] = df['total_value'].rolling(window=7).mean()
        df['ma_14'] = df['total_value'].rolling(window=14).mean()
        df['ma_21'] = df['total_value'].rolling(window=21).mean()
    
    def diff_yesterday_sales(self):
        df = self.dataframe
        df['diff_yesterday_sales'] = df['total_value'].diff()

    def lag_sales(self):
        df = self.dataframe
        df['lag1'] = df['total_value'].shift(1)
        df['lag7'] = df['total_value'].shift(7)
        df['lag14'] = df['total_value'].shift(14)
        df['lag21'] = df['total_value'].shift(21)
        df['lag28'] = df['total_value'].shift(28)

    def transform(self, holidays, comercialdays):
        self.is_holiday(holiday=holidays)
        self.is_commercial_day(list_date=comercialdays)
        self.day_of_week()
        self.day_of_month()
        self.day_of_year()
        self.moving_average()
        self.diff_yesterday_sales()
        self.lag_sales()
