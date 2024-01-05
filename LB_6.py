import sys
import math

def discrete_log_attack(g, h, q):
    m = int(math.sqrt(q - 1))
    hash_table = {}
    for j in range(m):
        hash_table[pow(g, j, q)] = j

    g_inverse_m = pow(g, -m, q)
    for i in range(m):
        temp = (h * pow(g_inverse_m, i, q)) % q
        if temp in hash_table:
            x = i * m + hash_table[temp]
            return x

g, h, q = [int(i) for i in input().split()]
result = discrete_log_attack(g, h, q)
print(result)
