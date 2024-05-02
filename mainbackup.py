import numpy as np
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
#md1 = pd.read_csv("PCOSTrain.csv")
md2 = pd.read_csv("VgSalesTrain.csv")
md2
md3 = pd.read_csv("HousesTrain.csv")
md3
#md4 = pd.read_csv("SalesTrain.csv")    

#reg1 = linear_model.LinearRegression()
#reg1.fit(md1[["Age", "Weight", "Height", "BG", "Pulse", "RR", "Hb", "Cycle", "CycleL", "MaStatus", "HCG1", "HCG2", "FSH", "LH", "Hip", "Waist", "TSH", "AMH", "PRL", "VITD3", "PRG", "RBS", "WeightG", "WeightL", ]],md1.PCOS)

reg2 = linear_model.LinearRegression()
reg2.fit(md2[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]],md2.Global_Sales)

reg21 = linear_model.LinearRegression()
reg21.fit(md2[[ "EU_Sales", "Other_Sales"]],md2.NA_Sales)
reg22 = linear_model.LinearRegression()
reg22.fit(md2[["NA_Sales", "JP_Sales", "Other_Sales"]],md2.EU_Sales)
reg23 = linear_model.LinearRegression()
reg23.fit(md2[["NA_Sales", "EU_Sales", "Other_Sales"]],md2.JP_Sales)
reg24 = linear_model.LinearRegression()
reg24.fit(md2[["NA_Sales", "EU_Sales", "JP_Sales"]],md2.Other_Sales)

reg3 = linear_model.LinearRegression()
reg3.fit(md3[["Area", "BHK", "Bathroom", "Age"]],md3.Price)

#reg4 = linear_model.LinearRegression()
#reg4.fit(md3[["a", "z", "y", "x"]],md4.b)

a = int(input("Please tell us what model would you like to use \n 1 = md1 \n 2 = md2 \n 3 = md3 \n 4 = md4 \n md1 and md4 are currently out of service."))

if a == 3:
    ar = float(input("Enter the Area of House (in sqft): "))
    bh = float(input("Enter the Number of Bedrooms + Hall + Kitchen in your house (BHk): "))
    bah = float(input("Enter the Number of Bathrooms in your House: "))
    ag = float(input("Enter the Age of your House: "))
    
    prf = reg3.predict([[ar , bh , bah , ag]])
    #print("Your House is worth ", prf, "rupees (in lacs)")
    #print(reg3.coef_)
    #print(reg3.intercept_)
    X = md3.iloc[:, :-1].values
    y = md3.iloc[:, 1].values
    
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=5, random_state=0)
    #y_pred = reg3.predict(X_test)
    plt.xlabel('area (sqft)')
    plt.ylabel('price (Rs. In Lacs)')
    plt.scatter(md3.Area, md3.Price, color='red',marker='+')
    #plt.scatter(X_train, y_train,color='g')
    #plt.plot(X_test, y_pred,color='k')


    plt.show()
elif a == 2:
    init = int(input("Hello! This is the VGSales model, I will help you forecast the sales of your game in a region based on how it has performed in other regions. \n Enter 1 for NA Prediction \n Enter 2 for EU Prediction \n Enter 3 for Japan Prediciton \n Enter 4 for Prediction in APAC Prediction"))
    if init == 1:
        EU = float(input("Enter your EU Sales"))
        #JP = float(input("Enter your JP Sales"))
        APAC = float (input("Enter your APAC Sales"))
        
        VGSalesF = reg21.predict([[EU , APAC]])
        
        print("The Sales Forecast is ", VGSalesF, "(in millions)")
        plt.xlabel('NA Sales (in millions)')
        plt.ylabel('Global Sales (in millions)')
        plt.scatter(md2.Global_Sales, md2.NA_Sales, color='red',marker='+')
        plt.show()
else:
    print("Out of Service")
    
