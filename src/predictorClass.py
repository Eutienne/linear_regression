from src.trainerClass import *

class Predictor:
    """
			Constructor
	"""
    def __init__(self):
        self.T1 = Trainer()
        if os.path.exists("data/TrainResults.json"):
            self.load_json()
    
    def load_json(self):
        with open("data/TrainResults.json", 'r') as file:
            dict_ = json.load(file)
        
        if 'theta0' and 'theta1' in dict_:
            self.T1.theta0 = dict_['theta0']
            self.T1.theta1 = dict_['theta1']