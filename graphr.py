import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from io import BytesIO

matplotlib.style.use('seaborn-white')

def graph_data(f,img_path):
    figfile = BytesIO()
    df = pd.read_csv(f, sep='\t', index_col=0, parse_dates=True)
    df.plot(subplots=True)
    plt.legend(bbox_to_anchor = (1.05,1), loc = 2)#'upper left')
    plt.savefig(figfile, format='svg')#, bbox_inches='tight')
    figdata_svg = b'<svg' + figfile.getvalue().split(b'<svg')[1]
    figdata_svg = figdata_svg.decode()
    plt.close()
    return figdata_svg
