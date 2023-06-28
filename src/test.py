while True:
    def testPrime(n):
        i = 2
        while i <= n**(1/2):
            if n % i == 0:
                return False
            i += 1
            return True
    n = int(input("Number : "))
    if testPrime(n):
        print("เป็นจำนวนเฉพาะ")
    else:
        print("ไม่เป็นจำนวนเฉพาะ")