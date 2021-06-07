import pickle


if __name__ == "__main__":
    myObj = {"0" : [1,2,3]}
    myObj = pickle.dump(myObj)

    print(myObj)

    myObj = pickle.load(myObj)

    print(myObj["0"])