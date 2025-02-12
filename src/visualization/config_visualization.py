import os
import enum
import matplotlib.pyplot as plt
from matplotlib import font_manager
from src.config_base import GeneralConfig

import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator, FixedLocator

def instantiate_matplotlib_parameters():
    #regular font
    font_path_regular = os.path.join(GeneralConfig.path2data_font.value, 'Arial.ttf')
    font_manager.fontManager.addfont(font_path_regular)
    prop = font_manager.FontProperties(fname=font_path_regular)
    # bold font
    font_path_bold = os.path.join(GeneralConfig.path2data_font.value, 'Arial_Bold.ttf')
    font_manager.fontManager.addfont(font_path_bold)
    prop = font_manager.FontProperties(fname=font_path_bold)

    SMALL_SIZE = 7  # size of the text
    MEDIUM_SIZE = 11
    BIGGER_SIZE = 12

    plt.rcParams.update({'font.size':SMALL_SIZE})  # controls default text sizes
    plt.rcParams.update({'axes.titlesize':SMALL_SIZE})  # fontsize of the axes title
    plt.rcParams.update({'axes.labelsize':SMALL_SIZE})  # fontsize of the x and y labels
    plt.rcParams.update({'xtick.labelsize':SMALL_SIZE})  # fontsize of the tick labels
    plt.rcParams.update({'ytick.labelsize':SMALL_SIZE})  # fontsize of the tick labels
    plt.rcParams.update({'legend.fontsize':SMALL_SIZE})  # legend fontsize
    plt.rcParams.update({'figure.titlesize':SMALL_SIZE})  # fontsize of the figure title
    
    # STIX
    plt.rcParams.update({'text.usetex':False})
    plt.rcParams.update({'mathtext.default': 'regular'})
    plt.rcParams.update({'font.family': 'sans-serif'})
    plt.rcParams.update({'font.sans-serif': "Calibri"})
    plt.rcParams.update({'mathtext.fontset':'custom'})
    plt.rcParams.update({'mathtext.rm':'Calibri'})
    plt.rcParams.update({'mathtext.bf':'Calibri:bold'})
    return

def cm2inch(value):
    return value/2.54

class VisualizationConfig(enum.Enum):
    """
    Holds the config values for the figure visualization
    """

    # TUM colors
    # primary colors
    TUMweiss = (1, 1, 1)
    TUMschwarz = (0, 0, 0)
    TUMblau = (0, 101 / 255, 189 / 255)

    # secondary colors
    TUMdunkelblau = (0, 82 / 255, 147 / 255)
    TUMdunkelblau2 = (0, 51 / 255, 89 / 255)

    TUMgrau80 = (51 / 255, 51 / 255, 51 / 255)
    TUMgrau50 = (156 / 255, 157 / 255, 159 / 255)
    TUMgrau20 = (217 / 255, 218 / 255, 219 / 255)

    TUMgrau = (218 / 255, 215 / 255, 203 / 255)
    TUMorange = (227 / 255, 114 / 255, 34 / 255)
    TUMgruen = (162 / 255, 173 / 255, 0 / 255)
    TUMhellblau = (152 / 255, 198 / 255, 234 / 255)
    TUMhellblau2 = (100 / 255, 160 / 255, 200 / 255)

    #values rounded down
    columnwidth_in_cm = 8.8
    columnsheight_in_cm_max = 13.0 

    textwidth_in_cm = 18.0
    textheight_in_cm_max = 18.5

    