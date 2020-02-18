N, K = map(int, input().split())
s = list(input())
s[K-1] = chr(ord("a")+ord(s[K-1])-ord("A"))
print("".join(s))