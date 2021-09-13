from os import name
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv("savings_data_final.csv")
q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)
iqr = q3-q1

print(f"Q1-{q1}")
print(f"Q3-{q3}")
print(f"IQR-{iqr}")

lower_whisker = q1-1.5*iqr
upper_whisker = q3-1.5*iqr

print(f"Lower Whisker-{lower_whisker}")
print(f"Upper Whisker-{upper_whisker}")

new_df = df[df["quant_saved"]<upper_whisker]

all_savings = df["quant_saved"].tolist()
print(f"Mean of savings-{statistics.mean(all_savings)}")
print(f"Median of savings-{statistics.median(all_savings)}")
print(f"Mode of savings-{statistics.mode(all_savings)}")
print(f"Standard deviation of savings-{statistics.stdev(all_savings)}")

fig = ff.create_distplot([df["quant_saved"].tolist()],["savings"],show_hist=False)
#fig.show()

sampling_mean_list = []
for i in range(1000):
    temp_list = []
    for j in range(100):
        temp_list.append(random.choice(all_savings))
    sampling_mean_list.append(statistics.mean(temp_list))
mean_sampling = statistics.mean(sampling_mean_list)

print(f"Mean of population{statistics.mean(all_savings)}")
print(f"Mean of sampling distribution{statistics.mean(sampling_mean_list)}")
temp_df = new_df[new_df.age!=0]
age = temp_df["age"].tolist()
savings = temp_df["quant_saved"].tolist()
correlation = np.corrcoef(age,savings)
print(f"Correlation between the age of the person and savings is-{correlation[0,1]}")

fig = ff.create_distplot([sampling_mean_list],["Savings(sampling)"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_sampling,mean_sampling],y=[0,0.1],mode="lines",name="MEAN"))
#fig.show()