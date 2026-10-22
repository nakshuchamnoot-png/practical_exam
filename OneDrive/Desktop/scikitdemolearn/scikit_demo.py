# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:32:03 2026

@author: Naksh
"""

from sklearn.linear_model import LinearRegression
hours = [[1],[2],[3],[4],[5]]
marks=[20,30,40,50,70]
model = LinearRegression()
model.fit(hours,marks)
predicted=model.predict([[6]])
print("Hours studies",6)
print("predict",predicted[0])