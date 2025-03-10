def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, num + 1):
        if prime[p]:
            primes.append(p)
    return primes

if __name__ == '__main__':
    num = 1000000
    primes = SieveOfEratosthenes(num)
	
    T = int(input())
    tes = []

    for i in range(T):	
        K = int(input())
        tes.append(K)

    for i in range(T):
        print(primes[tes[i] - 1]) 