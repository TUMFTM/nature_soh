from src.data.read_pickle import ReadPickle
import pandas as pd
import scipy as sp

class ReadFeather(ReadPickle):
    """
    Filter Methods
    """
    def __init__(self):
        super(ReadFeather, self).__init__()

    def read(self,path,  initial_cap = 0,resample=False,filter_cell_voltages=False,lower_voltage=0, upper_voltage=1000):
        df = pd.read_feather(path)
        if resample:
            df = self.resample_time(df,resample)
        df["I"] = self.filter_func_I(df["I"])
        df["U"] = self.filter_func_U(df["U"])
        df["Q"] = self.filter_func_Q(df["Q"])
        df = self.calc_E_from_P(df)
        if filter_cell_voltages:
            df = self.filter_cell_voltages(df)
        out = self.extract_between_voltages(df, lower_voltage, upper_voltage)
        # out = self.calc_Q_from_I(df,initial_cap)
        # in the data preperation the Q is already calculated from the current signal
        return out