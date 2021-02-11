def fib(n): #write fibonancci series up to n
    a, b = 0, 1
    while a < n:
        print (a, end=' ')
        a, b = b, a+b

def fib2(n): #return fibinancci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#Putri Ramadhanti/29/XI-5
