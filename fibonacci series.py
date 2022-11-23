def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence using recursive method:")
   for i in range(nterms):
       print(recur_fibo(i))

# Program to display the Fibonacci sequence using non recursive method.

print("Fibonacci sequence using recursive method:")
# n=int(input("Enter the number of terms needed "))

n = 10
a = 0
b = 1

print(a)
print(b)

while (n - 2):
    c = a + b
    a = b
    b = c
    print(c)
    n = n - 1
