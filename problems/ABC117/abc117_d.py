N, K = map(int, input().split())
*A, = map(int, input().split())

def get_k_bits():
    global K
    k_list = []
    while K:
        k_list.append(K%2)
        K//=2
    k_list.extend([0]*(50-len(k_list)))
    k_list.reverse()
    return k_list

def get_bits_count():
    b = [0]*50
    for i in A:
        p = 0
        while i:
            b[p] += i%2
            i //=2
            p += 1
    b.reverse()
    return b

b = get_bits_count()

def get_appropriate_bits():
    c = [0]*50
    for i in range(50):
        e, f = b[i], N-b[i]
        if e>=f:
            c[i] = 0
        else:            
            c[i] = 1
    return c

def output_candidates():
    candidates = []
    c = get_appropriate_bits()
    k_list = get_k_bits()

    for i in range(50):
        if k_list[i]:
            o = [k_list[j] for j in range(i)] + [0] + [c[j] for j in range(i+1, 50)]
            candidates.append(o)
    candidates.append(k_list)
    return candidates


ans = 0
for bits in output_candidates():
    v = 0
    for j in range(50):
        if bits[j]:
            v += (2**(50-j-1))*(N-b[j])
        else:
            v += (2**(50-j-1))*b[j]
    ans = max(ans, v)

print(ans)