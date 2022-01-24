import math
    

def get_data(inputfilename: str) -> list:
    datastring = open(inputfilename, 'r').read()#read inputfile
    lines = datastring.split('\n')#split different lines
    result = []
    for line in lines:
        data = line.split(' ')#read each number in a line
        result.append([int(num) for num in data])#turn number's string into integer
    return(result)


def analyze_data(data: list, option: str) -> float:
    if option == 'average':
        counts = 0
        total = 0
        for line in data:
            for num in line:
                counts += 1#number of samples + 1
                total += num#the sum
        return(total/counts)
    elif option == 'standard deviation':
        mean = analyze_data(data, 'average')
        total = 0
        counts = 0
        for line in data:
            for num in line:
                counts += 1 #number of samples + 1
                total += (num - mean) ** 2 #the sum of (x - xbar)^2
        var = total / counts #the variance
        return(math.sqrt(var))
        
    elif option == 'covariance':
        x = data[0]
        y = data[1]
        xbar = analyze_data([x], 'average')
        ybar = analyze_data([y], 'average')
        total = 0
        counts = len(x)
        for i in range(len(x)):
            total += (x[i] - xbar) * (y[i] - ybar)
        return(total / counts)
    elif option == 'correlation':
        x = data[0]
        y = data[1]
        n = len(x)
        cov = analyze_data(data, 'covariance')
        sdx = analyze_data([x], 'standard deviation')
        sdy = analyze_data([y], 'standard deviation')
        return(cov / (sdx * sdy))
    else:
        return(float("-inf"))
    

inputfilename = "example.txt"
dat = get_data(inputfilename)
print("Mean: ", analyze_data(dat, "average"))
print("Standard deviation: ", analyze_data(dat, "standard deviation"))
print("Covariance: ", analyze_data(dat, "covariance"))
print("Correlation: ", analyze_data(dat, "correlation"))
print("Wrong input: ", analyze_data(dat, "error"))
