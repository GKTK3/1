def knsp(w, wgt, val, n):
    if n == 0 or w == 0:
        return 0

    elif (wgt[n-1] > w):
        return knsp(w, wgt, val, n-1)

    else:
        return max(
            val[n-1] + knsp(w-wgt[n-1], wgt, val, n-1),
            knsp(w, wgt, val, n-1)
        )


val = [60, 100, 120]
wgt = [10, 20, 30]
w = 50

n = len(val)

max_val = knsp(w, wgt, val, n)
print(max_val)
