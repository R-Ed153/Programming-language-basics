currencyList = (1000,500,200,100,50,40,20,10,5,1)

def getBalance(paid:int,owed:int)->int:
    if(owed > paid):
        raise ValueError("Amount paid must be greater than or equal to amount owed")
    else:
        return paid - owed

def getChange(denominationList: list,balance: int)-> dict:
    result = dict()  
    for denomination in denominationList:
        counter  = 0
        while(balance >= denomination):
            balance -= denomination
            counter += 1
        if(counter): 
            result[denomination] = counter

    return result



if __name__ == "__main__":
    testBalance = getBalance(2500,691)
    print(getChange(currencyList,testBalance))

