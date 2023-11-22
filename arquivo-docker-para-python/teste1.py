print("Hello, World!")


# ///////////////////////////////////////////////////////////////////////////////
# bubble Short

def Bubble(ARR):
    for passnum  in range (len(ARR)-1,0,-1):
        for i in range (passnum):
            if ARR[i] > ARR[i+1]:
                temp = ARR[i]
                ARR[i] = ARR[i+1]
                ARR[i+1] = temp
                
ARR = [10,11,12,13,14,16,15]
Bubble(ARR)
print(ARR)
# ///////////////////////////////////////////////////////////////////////////////


#////////////////////////////////////////////////////
#Busca binaria

def busca_binaria(ARR, esquerda, direita, item):
    if direita >= esquerda:
        meio = esquerda + (direita - esquerda) // 2

        if ARR[meio] == item:
            return meio
        elif ARR[meio] > item:
            return busca_binaria(ARR, esquerda, meio - 1, item)
        else:
            return busca_binaria(ARR, meio + 1, direita, item)
    else:
        return -1 

ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(busca_binaria(ARR, 0, len(ARR) - 1, 8))

# ///////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////

# Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Exemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)

# ///////////////////////////////////////////////////////////////////////////////
#fibonacci

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Exemplo de uso para obter os primeiros 10 números da sequência de Fibonacci
n = 10
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)

#////////////////////////////////////////////////////////////////////////////////
