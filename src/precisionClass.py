from src.trainerClass import *

class Precision:
    """
			Constructor
	"""
    def __init__(self):
        self.T1 = Trainer()
        if not os.path.exists("data/TrainResults.json"):
            print("There are no training results")
            exit(0)
        self.load_json()
    
    def load_json(self):
        with open("data/TrainResults.json", 'r') as file:
            dict_ = json.load(file)
        
        if 'theta0' and 'theta1' and 'price' and 'mileage'  in dict_:
            self.T1.theta0 = dict_['theta0']
            self.T1.theta1 = dict_['theta1']
            self.T1.mileage = dict_['mileage']
            self.T1.price = dict_['price']
    def CalculatePrecision(self):
        self.MAE()
        self.MSE()
        self.MAPE()
        self.MPE()
    
    def MAE(self):
        mae = 0.0
        for i in range(len(self.T1.mileage)):
            mae += abs(self.T1.price[i] - self.T1.estimatePrice(self.T1.mileage[i]))
        mae = mae / len(self.T1.mileage)
        print( "\033[93mMean Absolute Error (MAE)             =",  "{:.2f}".format(mae))
    
    def MSE(self):
        mse = 0.0
        for i in range(len(self.T1.mileage)):
            mse += (self.T1.price[i] - self.T1.estimatePrice(self.T1.mileage[i])) **2
        mse = mse / len(self.T1.mileage)
        print("Mean Squere Error (MSE)               =",  "{:.2f}".format(mse))

    def MAPE(self):
        mape = 0.0
        for i in range(len(self.T1.mileage)):
            mape += abs(self.T1.price[i] - self.T1.estimatePrice(self.T1.mileage[i])) / self.T1.price[i]
        mape = mape / len(self.T1.mileage)
        print("Mean Absolute Percentage Error (MAE)  = %f%%" %mape)

    def MPE(self):
        mpe = 0.0
        for i in range(len(self.T1.mileage)):
            mpe += (self.T1.price[i] - self.T1.estimatePrice(self.T1.mileage[i])) / self.T1.price[i]
        mpe = mpe / len(self.T1.mileage)
        print("Mean Percentage Error (MAE)           = %f%%" %mpe, '\033[0m')