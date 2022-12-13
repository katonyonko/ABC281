import io
import sys

_INPUT = """\
6
4 1000000000
3 100000000
500 987654321
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
def id(m,n):
  return m*(m+1)//2+n
C=[1]
for i in range(N):
  C.append(1)
  for j in range(i):
    C.append((C[i*(i+1)//2+j]+C[i*(i+1)//2+j+1])%M)
  C.append(1)
  dp=[0]*(N-1)**2
  dp[0]=1
  p=[pow(2,i,M) for i in range(N**2)]
  pp=[]
  for j in range(N-2):
    pp.append(p[j+1]-1)
    for l in range(N-3):
      pp.append(pp[-1]*(p[j+1]-1)%M)
  for i in range(N-2):
    for j in range(i+1):
      for l in range(N-i-2):
        dp[(i+l+1)*(N-1)+l]=(dp[(i+l+1)*(N-1)+l]+C[id(N-i-2,l+1)]*dp[i*(N-1)+j]*p[(l+1)*l//2]*pp[j*(N-2)+l])%M
  ans=0
  for i in range(N-2):
    ans=(ans+(pow(2,i+1,M)-1)*dp[(N-2)*(N-1)+i])%M
  print(ans)