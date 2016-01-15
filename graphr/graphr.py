import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from io import BytesIO
import seaborn as sns
from datetime import datetime,timedelta
#matplotlib.style.use('seaborn-white')

def graph_data(f,img_path):
    df = pd.read_csv(f, sep='\t', index_col=0, parse_dates=True)
    now = df.index[-1]
    before = now - timedelta(minutes=10)
    df = df.between_time(start_time = before, end_time=now)

    with sns.color_palette("Paired"):
        ax = plt.subplot(311)
        ax.plot(df.index, df['Diode 1 Temp (C)'])
        ax.plot(df.index, df['Diode 1 Set Temp (C)'])
        ax.plot(df.index, df['Diode 2 Temp (C)'])
        ax.plot(df.index, df['Diode 2 Set Temp (C)'])
        ax.legend(bbox_to_anchor = (1,1), loc=2)
        ax = plt.subplot(312)
        ax.plot(df.index, df['Output Power (W)'])
        ax.plot(df.index, df['Set Power (W)'])
        ax.legend(bbox_to_anchor = (1,1), loc=2)
    with sns.color_palette():
        ax = plt.subplot(313)
        ax.plot(df.index, df['Current (A)'])
        ax.legend(bbox_to_anchor=(1,1), loc=2)


    figfile = BytesIO()
    plt.savefig(figfile, format='svg', bbox_inches='tight', pad_inches = 0.25)
    figdata_svg = b'<svg' + figfile.getvalue().split(b'<svg')[1]
    figdata_svg = figdata_svg.decode()
    plt.close()
    return figdata_svg
