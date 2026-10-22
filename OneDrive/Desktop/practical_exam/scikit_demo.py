# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:14:52 2026

@author: Naksh
"""
from sklearn.linear_model import LinearRegression

hours=[[1],[2],[3],[4],[5]]
marks=[20,30,40,50,60]

model=LinearRegression()
model.fit(hours,marks)
predict_model=model.predict([[6]])
print("Hours studied",6)
print("predicted marks",predict_model[0])