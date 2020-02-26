N = int(input())
*A, = map(int, input().split())
print("APPROVED" if all(map(lambda x:x%3==0 or x%5==0, filter(lambda x:x%2==0, A))) else "DENIED")