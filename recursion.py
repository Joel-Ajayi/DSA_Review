def fibonacci(n:int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
    
def factorial(n:int)-> int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def findMaxofArr(n, arr:list[int]):
    if n == 1:
        return arr[0]
    return max(arr[-1], findMaxofArr(n-1, arr))   
print([fibonacci(i) for i in range(4)])
print(factorial(4))
print(findMaxofArr(4, [fibonacci(i) for i in range(4)]))