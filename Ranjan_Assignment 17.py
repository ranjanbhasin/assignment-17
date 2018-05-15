# -*- coding: utf-8 -*-
"""
Created on Tue May 15 23:45:39 2018

@author: Ranjan48833
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn
from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

from sklearn.metrics import classification_report

Url="https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/titanic
-train.csv"

titanic = pd.read_csv(url)
titanic.columns = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','E
mbarked']