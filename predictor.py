from src.predictorClass import *

if __name__ == "__main__":
    P = Predictor()
    mileage = float(input("Enter your mileage\n"))

    while mileage < 0:
        mileage = float(input("Enter your mileage\n"))
    if (P.T1.estimatePrice(mileage) < 0):
        print("0.00")
    else:
        print("{:.2f}".format(P.T1.estimatePrice(mileage)))