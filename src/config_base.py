import os
import enum

class GeneralConfig(enum.Enum):
    """
    Holds the general config values for the charge.COM repository
    """
    path2repository = os.path.join(os.getcwd().partition('nature_soh')[0], "nature_soh")

    
    path2data = os.path.join(path2repository, "data")
    path2data_font = os.path.join(path2repository, "data", "font")
    path2figures = os.path.join(path2repository,  "figures")