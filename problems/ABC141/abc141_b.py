S = input()
a = map(lambda x:x in {"L","U","D"},S[1::2])
b = map(lambda x:x in {"R","U","D"},S[0::2])
print("Yes" if sum(a)+sum(b)==len(S) else "No")