import io
import sys

_INPUT = """\
6
3
12 18 11
10
0 0 0 0 0 0 0 0 0 0
5
324097321 555675086 304655177 991244276 9980291
2
1 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import sys
  sys.setrecursionlimit(10**6)
  N=int(input())
  A=list(map(int,input().split()))
  A=list(set(A))
  memo={}
  def rec(A,n,k):
    if k in memo: return memo[k]
    if n==0:
      if len(A)==2:
        memo[k]=max(A)
        return memo[k]
      if A[0]&1==1:
        memo[k]=A[0]^1
        return A[0]^1
      memo[k]=A[0]
      return A[0]
    x,y=[],[]
    for i in range(len(A)):
      if (A[i]>>n)&1==1: x.append(A[i])
      else: y.append(A[i])
    if len(x)==0:
      memo[k]=rec(y,n-1,k)
    elif len(y)==0:
      for i in range(len(x)):
        x[i]^=1<<n
      memo[k]=rec(x,n-1,k^(1<<n))
    else:
      for i in range(len(y)):
        y[i]^=1<<n
      memo[k]=min(rec(x,n-1,k),rec(y,n-1,k^(1<<n)))
    return memo[k]
  print(rec(A,29,1<<30))