import math
import matplotlib.pyplot as plt
import numpy as np

theta0, theta1 = 0.0, 0.0
mse = []

def readfile():
    data = []
    with open("data.csv", "r") as f:
        lines = f.readlines()[1:]
    for line in lines:
        data.append([int(s) for s in line.rstrip().split(',') if s.isdigit()])
    mileage, price = zip(*data)
    return mileage, price

def Relements(mileage, price, xAverage, yAverage):
    tmpx, x2, tmpy, y2, sumxy = 0.0, 0.0, 0.0, 0.0, 0.0
    for index in range(len(mileage)):
        tmpx = mileage[index] - xAverage
        tmpy = price[index] - yAverage
        x2 += tmpx * tmpx
        y2 += tmpy * tmpy
        sumxy += tmpx * tmpy
    length = len(price)
    return sumxy / length, x2 / length, y2 /length

def Average(lst):
    return sum(lst) / len(lst)

def getLearningRate(mileage, price):
    xAverage = Average(mileage)
    yAverage = Average(price)
    sumxAverage, x2Average, y2Averege = Relements(mileage, price, xAverage, yAverage)
    # tmp1 = math.sqrt(y2Averege / (len(price) - 1)) / math.sqrt(x2Average / (len(mileage) - 1))
    return sumxAverage / math.sqrt(x2Average * y2Averege) * -1

def denormalize(mileage, price):
    xMax = float(max(mileage))
    xMin = float(min(mileage))
    yMax = float(max(price))
    yMin = float(min(price))
    global theta1, theta0
    theta1 *= ((yMax - yMin) / (xMax - xMin))
    theta0 = ((yMax - yMin) *theta0) + (theta1 * (1 - xMin) +yMin)

def normalize(data):
    minVal = float(min(data))
    maxVal = float(max(data))
    newList = []

    for i in data:
        newList.append(float (i - minVal) / (maxVal - minVal))
    return newList

def estimatePrice(mileage):
    return theta0 + (theta1 * mileage)

def train(mileage, price):
    tmp0, tmp1, tmp2 = 0.0, 0.0, 0.0
    normMileage = normalize(mileage)
    normPrice = normalize(price) 
    for i in range(len(mileage)):
        tmp0 += estimatePrice(normMileage[i]) - normPrice[i] 
        tmp1 += (estimatePrice(normMileage[i]) - normPrice[i]) * normMileage[i]
        tmp2 += (estimatePrice(normMileage[i]) - normPrice[i]) *  (estimatePrice(normMileage[i]) - normPrice[i])

    # print(tmp0 * tmp0)
    global mse
    mse.append(float(tmp2 / len(mileage)))
    
    global theta0, theta1
    theta0 -= learningRate * tmp0/len(mileage)
    theta1 -= learningRate * tmp1 / len(price)

if __name__ == "__main__":
    mileage, price = readfile()
    learningRate = getLearningRate(mileage, price)
    for i in range(1000):
        train(mileage,price)
    denormalize(mileage, price)

    km_norm = normalize(mileage)
    km_price = normalize(price)

    plt.scatter(mileage, price)
    plt.title('The car price vs mileage', fontsize=20)
    plt.xlabel('mileage', fontsize=18)
    plt.ylabel('price', fontsize=18)
    # plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    x = np.array(range(240000))
    y = theta0 + theta1 * x

    plt.plot(x, y)
    
    plt.show()
    x = np.array(range(len(mse)))
    y = mse
    # plt.xlim(xmin= -1)
    # global mse
    plt.plot(x, y)
    plt.show()
    # print(len(mse))
    # print(mse)