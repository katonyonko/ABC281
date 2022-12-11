import io
import sys

_INPUT = """\
6
3 600
180 240 120
3 281
94 94 94
10 5678912340
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
1 101
3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,T=map(int,input().split())
  A=list(map(int,input().split()))
  T%=sum(A)
  ans=0
  while T>A[ans]: T-=A[ans]; ans+=1 
  print(ans+1,T)