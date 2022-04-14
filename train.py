from src.trainerClass import *
from src.Graphs import *

def path_exist():
    if not os.path.exists("data/data.csv"):
        print("data.csv does not exists")
        exit(0)

if __name__ == "__main__":
    path_exist()
    T1 = Trainer("data/data.csv")
    T1.train()
    Graphs_Linear(T1,'The car price vs mileage','mileage','price')
    Graphs_Norm(T1,'The car price vs mileage norm','mileage','price')
    Graphs_MSE(T1,'Mean Squared Error','iterations','error', len(T1.mse))
    
    T1.save_json("data/TrainResults.json")

