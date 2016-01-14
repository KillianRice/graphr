import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
f = 'data.txt'
df = pd.read_csv(f,sep='\t', index_col=0, parse_dates=True)
df.plot()
plt.show()
