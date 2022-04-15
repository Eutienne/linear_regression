from src.predictorClass import *

if __name__ == "__main__":
    P = Predictor()
    mileage = -1

    while mileage < 0:
        try:
            mileage = float(input("Enter your mileage\n"))
        except:
            print("Error, mileage must be number")
            exit(0)
    if (P.T1.estimatePrice(mileage) < 0):
        print("0.00")
    else:
        print("{:.2f}".format(P.T1.estimatePrice(mileage)))