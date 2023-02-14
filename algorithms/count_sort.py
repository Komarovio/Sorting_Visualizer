def count_sort():
    n = int(input())
    A = [int(m) for m in input().split()]
    A_sort = [0 for m in range(n)]
    M = max(A)
    B = [0 for m in range(M)]
    for j in range(n):
        B[A[j] - 1] += 1
    for i in range(1, M):
        B[i] += B[i - 1]
    for j in range(n - 1, -1, -1):
        A_sort[B[A[j] - 1] - 1] = A[j]
        B[A[j] - 1] -= 1
    print(*A_sort)
