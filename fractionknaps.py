class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fabknsp(W, arr):
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)

    finalValue = 0.0

    for i in arr:
        if i.weight <= W:
            W -= i.weight
            finalValue += i.value

        else:
            finalValue += i.value * W / i.weight

    return finalValue


W = 50
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

max_val = fabknsp(W, arr)
print(max_val)
