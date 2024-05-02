import numpy as np
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

md5 = pd.read_csv("VgSalesTrain.csv")

reg5 = linear_model.LinearRegression()
reg5.fit(md5[["NA_Sales", "EU_Sales", "Other_Sales", "Sports", "Platform", "Racing", "Role-Playing", "Puzzle", "Misc", "Shooter", "Simulation", "Fighting", "Action", "Strategy", "Adventure"]],md5.Global_Sales)


