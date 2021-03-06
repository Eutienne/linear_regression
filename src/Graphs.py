import matplotlib.pyplot as plt
import numpy as np
import os


def Graphs_Linear(T1, title, xlabel, ylabel, length=240000):
    plt.scatter(T1.mileage, T1.price, color='navy')
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    x = np.array(range(length))
    y = T1.theta0 + T1.theta1 * x
    plt.plot(x, y, color='lightseagreen')
    if not os.path.isdir("Graphs"):
        os.makedirs("Graphs")
    plt.savefig('Graphs/Linear_Regression.png')
    plt.close()
    # plt.show()

def Graphs_Norm(T1, title, xlabel, ylabel, length=2):
    plt.scatter(T1.km_norm, T1.pr_norm, color='fuchsia')
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    x = np.array(range(length))
    y = T1.normtheta0 + T1.normtheta1 * x
    plt.ylim(0)
    plt.plot(x, y, color='purple')
    if not os.path.isdir("Graphs"):
        os.makedirs("Graphs")
    plt.savefig('Graphs/Linear_Regression_Norm.png')
    plt.close()
    # plt.show()

def Graphs_MSE(T1, title, xlabel, ylabel, length):
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    x = np.array(range(length))
    y = T1.mse
    plt.plot(x, y, color='crimson')
    if not os.path.isdir("Graphs"):
        os.makedirs("Graphs")
    plt.savefig('Graphs/Mean_Squared_Error.png')
    plt.close()