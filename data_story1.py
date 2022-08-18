from google.colab import files
a = files.upload()
import pandas as pd 
import plotly.figure_factory as ff
import csv
import plotly.graph_objects as go
import plotly.express as pe
import statistics
import numpy as np

df = pd.read_csv("data.csv")
fig = pe.scatter(df, y="quant_saved")
fig.show()
with open("data.csv") as f:
  reader = csv.reader(f)
  saving_data = list(reader)
saving_data.pop(0)
total_entry = len(saving_data)
tpgr = 0
for data in saving_data:
  if(int(data[3])==1):
    tpgr += 1
import plotly.graph_objects as go   
fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[tpgr, (total_entry - tpgr)])) 

all_saving = []
for data in saving_data:
  all_saving.append(float(data[0]))
mean = statistics.mean(all_saving)
median = statistics.median(all_saving)
mode = statistics.mode(all_saving)
print(mean, median, mode)

r_saving=[]
nr_saving=[]
for data in saving_data:
  if(int(data[3])==1):
    r_saving.append(float(data[0]))
  else:
    nr_saving.append(float(data[0]))

mean = statistics.mean(r_saving)
median = statistics.median(r_saving)
mode = statistics.mode(r_saving)
print(mean, median, mode)

mean = statistics.mean(nr_saving)
median = statistics.median(nr_saving)
mode = statistics.mode(nr_saving)
print(mean, median, mode)

st_dev_r = statistics.stdev(r_saving)
st_dev_nr = statistics.stdev(nr_saving)
st_dev_all = statistics.stdev(all_saving)
print(st_dev_r,st_dev_nr,st_dev_all)

gender =[]
savings=[]
for data in saving_data:
  if(float(data[5])==1):
    gender.append(float(data[5]))
    savings.append(float(data[0]))
correlation=np.corrcoef(gender,savings)
print(correlation) 