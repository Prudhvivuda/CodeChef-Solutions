You are an administrator of a popular quiz website. Every day, you hold a quiz on the website.

There are N users (numbered 1 through N) and M admins (numbered N+1 through N+M). For each quiz, each user is allowed to attempt it at most once. Sometimes, admins attempt the quizzes for testing purposes too; an admin may attempt a quiz any number of times.

On a certain day, the quiz was attempted K times. For each i (1≤i≤K), the i-th of these attempts was made by the person with number Li. Find all the users who attempted the quiz more than once, in order to disqualify them.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains three space-separated integers N, M and K.
The second line contains K space-separated integers L1,L2,…,LK.
Output
For each test case, print a single line containing an integer D denoting the number of users who should be disqualified, followed by a space and D space-separated integers denoting their numbers in ascending order.

Constraints
1≤T≤10
0≤N,M≤105
1≤N+M,K≤105
1≤Li≤N+M for each valid i
Example Input
3
1 1 1
1
1 1 2
1 1
5 5 10
2 5 2 5 2 4 10 10 10 10
Example Output
0
1 1
2 2 5
Explanation
Example case 1: Since there is only a single attempt during the whole day, there cannot be any user who made more than one attempt.
Example case 2: User 1 attempted the quiz twice.
Example case 3: Users 2 and 5 attempted the quiz multiple times. The admin with number 10 also attempted the quiz multiple times, but admins are allowed to do that.

____________________________________________________________________________________________________________________________

# SOLUTION

from collections import Counter
for _ in range(int(input())):
    n, m, k = map(int,input().split())
    kl = [int(i) for i in input().split()]
    h = Counter(kl)
    ans = []
    cnt = 0
    for i in h:
        if i<=n and h[i]>1:
            cnt += 1
            ans.append(i)
    ans.sort()
    print(cnt,*ans) if ans else print(0)
