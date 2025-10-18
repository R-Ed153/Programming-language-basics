def numberOfTimesDivisibleBy2(n:int)->int:
    counter = 0
    while(n >= 2):
        n = n // 2
        counter += 1
    return counter


if(__name__ == "__main__"):
    while True:
        userInput = int(input("Enter a positive number to find out how mainy times 2 can be divided from it: \n"))
        print(numberOfTimesDivisibleBy2(userInput))