A = [1, 5, 5]
B = [1, 1, 1, 2, 5]
C = A + B

C.sort()

S = 0
i = 1
N = len(A)
while i <= N and C[i] <= S + 1:
    S += C[i]
    i += 1

if S >= sum(A):
    print(None)
else:
    print(sum(A[:N - S]))
