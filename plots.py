import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 100)

m2014 = pd.read_csv("metric_2014.csv")
m2015 = pd.read_csv("metric_2015.csv")
m2016 = pd.read_csv("metric_2016.csv")
m2017 = pd.read_csv("metric_2017.csv")
m2018 = pd.read_csv("metric_2018.csv")
m2019 = pd.read_csv("metric_2019.csv")
m2020 = pd.read_csv("metric_2020.csv")
m2021 = pd.read_csv("metric_2021.csv")

a = dict()
arr = np.empty((100,8))
name = ["m2014","m2015","m2016","m2017","m2018","m2019","m2020","m2021",]
for j in name:
    var = globals()[j]
    print(j)
    labels = []
    model = kmeans.fit(globals()[j].iloc[:,[1,2,3]].values)
    #model.predict(globals()[j].iloc[:,[1,2,3]].values)
    labels = model.labels_
    for i in labels:
        arr[i][name.index(j)] = arr[i][name.index(j)]+1

figure,axis = plt.subplots(3,2,figsize = (12,12))
axis[0,0].plot(name,arr[-1])
axis[0,0].set_title("100th")

axis[0,1].plot(name,arr[0])
axis[0,1].set_title("1st")

axis[1,0].plot(name,arr[-2])
axis[1,0].set_title("99th")

axis[1,1].plot(name,arr[1])
axis[1,1].set_title("2nd")

axis[2,0].plot(name,arr[-3])
axis[2,0].set_title("98th")

axis[2,1].plot(name,arr[2])
axis[2,1].set_title("3rd")