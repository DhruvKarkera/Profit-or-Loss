#Python 3 program to demonstrate
#Profit & Loss

#Function to calculate Profit
from cmath import cos


def Profit(costPrice,sellingPrice) :
    profit = (sellingPrice - costPrice)
    
    return profit

#Function to calculate Loss

def Loss(costPrice,sellingPrice):
    
    loss = (costPrice - sellingPrice)
    
    return loss

#Drive Code

if __name__ == "__main__" :
    
    costPrice= int(input("Please enter a cost price : "))
    sellingPrice= int(input("Please enter a selling price : "))
    
    if sellingPrice == costPrice :
        print("No profit nor loss!")
    elif sellingPrice > costPrice :
        print("Rs", Profit(costPrice,sellingPrice),"Profit")
    else :
        print("Rs", Loss(costPrice,sellingPrice),"Loss")
