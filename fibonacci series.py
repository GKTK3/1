#  recursive
# using DP
def fibo(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]


def fab(n):
    if n <= 1:
        return n

    return (fab(n-1) + fab(n-2))


n = 9
print(fab(n))
