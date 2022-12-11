import io
import sys

_INPUT = """\
6
4 2 2
1 2 3 4
3 1 2
1 3 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def id(i,j,k):
    return i*(K+1)*D+j*D+k
  N,K,D=map(int,input().split())
  A=list(map(int,input().split()))
  dp=[-1]*((N+1)*(K+1)*D)
  dp[id(0,0,0)]=0
  for i in range(N):
    for j in range(K+1):
      for k in range(D):
        dp[id(i+1,j,k)]=max(dp[id(i+1,j,k)],dp[id(i,j,k)])
    for j in range(1,K+1):
      for k in range(D):
        if dp[id(i,j-1,k)]!=-1:
          dp[id(i+1,j,(k+A[i])%D)]=max(dp[id(i+1,j,(k+A[i])%D)],dp[id(i,j-1,k)]+A[i])
  print(dp[id(N,K,0)])