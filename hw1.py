def get_data(path: str) -> list:
    result = []
    with open(path, 'r') as f:
        for line in f:
            result.append(list(map(float, line.split(' '))))
    return result


def analyze_data(lists: list, methodname: str) -> float:
    number = []
    for i in lists:
        for j in i:
            number.append(j)

    if methodname == "average":
        print(sum(number)/ len(number))

    if methodname == "standard deviation":
        mean = sum(number) / len(number)
        print((sum([(x - mean)**2 for x in number])/len(number))**0.5)

    if methodname == "covariance":
        mean_0 = sum(lists[0]) / len(lists[0])
        mean_1 = sum(lists[1]) / len(lists[1])
        sub_0 = [i - mean_0 for i in lists[0]]
        sub_1 = [i - mean_1 for i in lists[1]]
        numerator = sum([sub_0[i]*sub_1[i] for i in range(len(sub_0))])
        denominator = len(lists[0])
        print(numerator / denominator)

    if methodname == "correlation":
        mean_0 = sum(lists[0]) / len(lists[0])
        mean_1 = sum(lists[1]) / len(lists[1])
        sub_0 = [i - mean_0 for i in lists[0]]
        sub_1 = [i - mean_1 for i in lists[1]]
        numerator = sum([sub_0[i] * sub_1[i] for i in range(len(sub_0))])
        std_0 = sum(sub_0[i]**2 for i in range(len(sub_0)))
        std_1 = sum(sub_1[i]**2 for i in range(len(sub_1)))
        denominator = (std_0*std_1)**0.5
        print(numerator / denominator)
