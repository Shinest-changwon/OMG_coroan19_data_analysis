# -*- coding: utf-8 -*-
"""time.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qvyDQvnwC_oVekOzxuLACBqgpb_3QqjQ
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as py

pi = pd.read_csv('./drive/My Drive/Colab Notebooks/dress_up/corona_visualization/PatientInfo.csv')
time = pd.read_csv('./drive/My Drive/Colab Notebooks/dress_up/corona_visualization/Time.csv')

time

test_new_list, negative_new_list, confirmed_new_list, released_new_list, deceased_new_list = list(), list(), list(), list(), list()
for i in range(len(time['test'])):
    if i == 0:
        test_new_list.append(time['test'][0])
    else:
        j = time['test'][i] - time['test'][i-1]
        test_new_list.append(j)

for i in range(len(time['negative'])):
    if i == 0:
        negative_new_list.append(time['negative'][0])
    else:
        j = time['negative'][i] - time['negative'][i-1]
        negative_new_list.append(j)

for i in range(len(time['time'])):
    if i == 0:
        confirmed_new_list.append(time['time'][0])
    else:
        j = time['time'][i] - time['time'][i-1]
        confirmed_new_list.append(j)

for i in range(len(time['released'])):
    if i == 0:
        released_new_list.append(time['released'][0])
    else:
        j = time['released'][i] - time['released'][i-1]
        released_new_list.append(j)

for i in range(len(time['deceased'])):
    if i == 0:
        deceased_new_list.append(time['deceased'][0])
    else:
        j = time['deceased'][i] - time['deceased'][i-1]
        deceased_new_list.append(j)

time['test_new'] = test_new_list
time['negative_new'] = negative_new_list
time['confirmed_new'] = confirmed_new_list
time['released_new'] = released_new_list
time['deceased_new_list'] = deceased_new_list

time

#csv 파일 저장
import csv

time.to_csv("./drive/My Drive/time_modified.csv")

