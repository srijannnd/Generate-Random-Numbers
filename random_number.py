from time import time


def random_num():
    v = str(time() - float(str(time()).split('.')[0]))
    num = round(int(v[len(v)-2:len(v)])/10)
    if num == 0:
        num = 1
    try:
        with open('filename.txt', 'r') as f:
            file = list(map(int, f.read().split(',')))
    except:
        f = open("filename.txt", "w+")
        f.write(str(num))
        with open('filename.txt', 'r') as f:
            file = list(map(int, f.read().split(',')))
    greater_numbers = list(filter(lambda x: x >= 5, file))
    if (len(greater_numbers) > 0.7*len(file) and num >= 5) or (len(greater_numbers) < 0.7*len(file) and num < 5):
        return random_num()
    else:
        with open("filename.txt", "a") as myfile:
            myfile.write(","+str(num))
    return num

