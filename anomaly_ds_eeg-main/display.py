import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math 
import time
from IPython.display import display, clear_output

data_set_path = 'anomaly_ds_eeg-main/NeurIPS-ts/data/01234.csv'
window_size = 70
display_delay = 2
sample_no = 5

df = pd.read_csv(data_set_path)

start_points = np.random.randint(df.shape[0]-window_size, size=sample_no)

samples = df.loc[start_points]
samples['start_point'] = start_points
samples.drop(columns=['value'], inplace=True)
samples = samples.reset_index()

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) 
for i in range(sample_no):
    ax.cla()
    ax.axes.get_yaxis().set_visible(False)
    ax.axes.get_xaxis().set_visible(False)
    ax.plot(df[samples['start_point'][i]:samples['start_point'][i]+window_size].reset_index()['value'])
    # display(fig)
    # clear_output(wait = True)
    time.sleep(display_delay)
    plt.show()