import math

theta0, theta1 = 0.0, 0.0

def readfile():
    lines = []
    data = []
    with open("data.csv", "r") as f:
        lines = f.readlines()[1:]
    for line in lines:
        data.append([int(s) for s in line.rstrip().split(',') if s.isdigit()])
    mileage, price = zip(*data)
    return mileage, price

def Relements(mileage, price, xAverage, yAverage):
    tmpx, x2, tmpy, y2, sumxy = 0.0, 0.0, 0.0, 0.0, 0.0
    index = 0
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
    tmp1 = math.sqrt(y2Averege / (len(price) - 1)) / math.sqrt(x2Average / (len(mileage) - 1))
    return sumxAverage / math.sqrt(x2Average * y2Averege) * -1

def estimatePrice(mileage):
    return theta0 + (theta1 * mileage)

def train(mileage, price):
    tmp0, tmp1 = 0.0, 0.0 
    for i in range(len(mileage)):
        tmp0 += estimatePrice(mileage[i]) - price[i] 
        tmp1 += (estimatePrice(mileage[i]) - price[i]) * mileage[i]
        print(tmp0, tmp1)
    
    global theta0 
    theta0 -= learningRate * tmp0/len(mileage)
    # theta0 -= (tmp0 / len(mileage) * learningRate)
    global theta1 
    theta1 -= learningRate * tmp1 / len(price)
    # theta1 -= (tmp1 / len(price) * learningRate)
    print(theta0 , theta1)

if __name__ == "__main__":
    mileage, price = readfile()
    learningRate = getLearningRate(mileage, price)
    for i in range(5):
        train(mileage,price)
    # print(learningRate, theta1, theta0)
    # print(theta0 - theta1 * 240000)
    # print(price)


# func estimatePrice(....):
#     return theta0 + theta1*km


# for i in 100:
#     tmp, tmp1 = learning(data)
#     update theta0 & theta1


# learnning(data):
#     for i in data
#         tmp +=  estimatePrice(i[0]) - i[1]
#         tmp1 += (estimatePrice(i[0]) - i[1]) * i[0]

#     tmp = tmp * (1/m) *learningRate
#     tmp1 = tmp1 / m * learningRate
#     return tmp tmp1
