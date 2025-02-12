import numpy as np
import pandas as pd
import scipy as sp
from src.filtering.config_filtering import FilteringConfig

class ReadPickle():
    """
    Filter Methods
    """
    def __init__(self):
        # default no filtering input = output
        self.filter_func_I = lambda x: x
        self.filter_func_U = lambda x: x
        self.filter_func_Q = lambda x: x

    def set_filter_I(self, filter_func):
        # default no filtering input = output
        self.filter_func_I = filter_func
        return

    def set_filter_U(self, filter_func):
        # default no filtering input = output
        self.filter_func_U = filter_func
        return

    def set_filter_Q(self, filter_func):
        # default no filtering input = output
        self.filter_func_Q = filter_func
        return

    def calc_Q_from_I(self,df,initial_cap=0):
        # initial in the function cumtrapz is only the first value ?!
        # what I wanted is an offset for the whole signal
        df["Q_calc"] = sp.integrate.cumtrapz(df["I"], df["time_h"], initial=0) + initial_cap
        return df
        
    def calc_E_from_P(self,df,initial_e=0):
        # initial in the function cumtrapz is only the first value ?!
        # what I wanted is an offset for the whole signal
        P = df["U"]*df["I"]
        df["E"] = sp.integrate.cumtrapz(P/1000, df["time_h"], initial=0) + initial_e
        return df

    def filter_cell_voltages(self,df):
        cell_volt_cols =  [col for col in df.columns if "cell_voltage" in col]
        for cell in cell_volt_cols:
            df[cell] = self.filter_func_U(df[cell])
        return df

    def resample_time(self,df,timedelta_s=5):
        df['date'] = pd.to_datetime(df['time_s'], unit='s')
        df.set_index("date",inplace=True)
        timedelta_string = str(timedelta_s)+"s"
        df = df.resample(timedelta_string).first()
        df.reset_index(inplace=True)
        df.drop(columns=["date"], inplace=True)
        return df

    def extract_between_voltages(self,df,lower_voltage=0,upper_voltage=1000):
        df = df[(df["U"] >= lower_voltage) & (df["U"] <= upper_voltage)]
        df["Q"] = df["Q"]-df["Q"].iloc[0] # reset Q counter
        df["E"] = df["E"]-df["E"].iloc[0] # reset E counter
        return df

    def read(self,path,  initial_cap = 0,resample=False,lower_voltage=0, upper_voltage=1000):
        df = pd.read_pickle(path)
        if resample:
            df = self.resample_time(df,resample)
        df["I"] = self.filter_func_I(df["I"])
        df["U"] = self.filter_func_U(df["U"])
        df["Q"] = self.filter_func_Q(df["Q"])
        df_filt = self.filter_cell_voltages(df)
        out = self.extract_between_voltages( df_filt, lower_voltage, upper_voltage)
        # out = self.calc_Q_from_I(df,initial_cap)
        # in the data prep the Q is already calculated from the current signal
        return out
