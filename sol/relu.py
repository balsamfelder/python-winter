def relu(x):
    if type(x) == int or type(x) == float:
        return x if x > 0 else 0
    elif type(x) == list:
        return [relu(i) for i in x]
