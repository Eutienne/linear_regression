
def readfile():
    lines = []
    data = []
    with open("data.csv", "r") as f:
        lines = f.readlines()[1:]
    
    for line in lines:
        data.append([int(s) for s in line.rstrip().split(',') if s.isdigit()])
    print(data)


if __name__ == "__main__":
    readfile()