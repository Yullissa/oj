def primePalindrome(N):
    """
    :type N: int
    :rtype: int
    """

    def isPrime(N):
        if (N <= 2 or N % 2 == 0):
            return N == 2
        for i in range(3, int(N ** 0.5) + 1, 2):
            if (N % i == 0):
                return False
        return True

    if 8 <= N <= 11: return 11

    for x in range(pow(10, len(str(N)) // 2), 100000):
        s = int(str(x) + str(x)[-2::-1])
        if s >= N and isPrime(s):
            return s


primePalindrome(1)
