def findP(a, b):
    mod = pow(10,9) + 7
    ans = 1
#   binary exponentiaton
    while b:
        if b%2 :ans = (ans*a)%mod
        a = (a*a)%mod
        b >>= 1
    return ans
    
for _ in range(int(input())):
    N, M = map(int, input().split())
    ans = findP((findP(2,N)-1),M)
    ans1 = (pow(10,9))+7
    ans = ans%ans1
    print(ans)
