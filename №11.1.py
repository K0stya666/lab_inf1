def f(A):
    A = str(A)
    if A.count('1')+A.count('0')!=len(A): return None
    ryad_fib = [1, 1]
    for i in range(len(A)):
        ryad_fib.append(ryad_fib[-1] + ryad_fib[-2])
    A = A[-1::-1]
    res = 0
    ryad_fib=ryad_fib[1:]
    for i in range(len(A)-1,-1,-1):
        res += ryad_fib[i] * int(A[i])
    return res

def Zeck_sys(A):
    if A == 0: return 0
    ryad_fib = [1, 1]
    while ryad_fib[-1] < A:
        ryad_fib.append(ryad_fib[-1] + ryad_fib[-2])
    ryad_fib = [ryad_fib[x] for x in range(len(ryad_fib)-1,0,-1) if ryad_fib[x] <= A]
    res = ''
    s = 0
    for i in ryad_fib:
        if A >= s + i:
            s+=i
            res += '1'
        else:
            res+='0'

    return res

A = 144
B = 10
C = 'Fib'

print("Ответ на задание 11 из десятичной в фиб:",Zeck_sys(A))
print("Введите число ")
A = int(input())

print(Zeck_sys(A))

B = 10000000000
print("Ответ на задание 11 из фиб в десятичную:",f(B))
B = int(input())
print(f(B))
