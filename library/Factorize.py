from collections import Counter


class Factorize:
    def __init__(self):
        self.primes = Counter()

    def add_target(self, n):
        for i in range(2, int(n**0.5)+1):
            while n%i==0:
                self.primes[i] += 1
                n //= i
            if not n:
                break
        if n>1:
            self.primes[n] += 1
    
    def get_result(self):
        return dict(self.primes)


if __name__ == "__main__":
    # 10の階乗を素因数分解するサンプル

    f = Factorize()
    for i in range(1, 10+1):
        f.add_target(i)
    
    d = f.get_result()
    print(d)