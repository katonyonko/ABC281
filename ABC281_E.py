import io
import sys

_INPUT = """\
6
6 4 3
3 1 4 1 5 9
10 6 3
12 2 17 11 19 8 4 3 6 20
20 4 2
1 2 2 11 13 3 4 5 61 2 34 7 6 9 5 6 77 8 21 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappush, heappop
  N,M,K=map(int,input().split())
  A=list(map(int,input().split()))
  tmp=sorted([(A[i],i) for i in range(M)])
  ans=sum([tmp[i][0] for i in range(K)])
  h,h2=[],[]
  for i in range(M-K): heappush(h,tmp[K+i])
  for i in range(K): heappush(h2,(-tmp[i][0],tmp[i][1]))
  using=set(tmp[:K])
  ans2=[]
  ans2.append(ans)
  for i in range(N-M):
    heappush(h,(A[i+M],i+M))
    if (A[i],i) in using:
      ans-=A[i]
      using.remove((A[i],i))
      x,y=heappop(h)
      while y<=i: x,y=heappop(h)
      ans+=x
      using.add((x,y))
      heappush(h2,(-x,y))
    else:
      x,y=heappop(h)
      while y<=i: x,y=heappop(h)
      z,w=heappop(h2)
      while w<=i: z,w=heappop(h2)
      if x<-z:
        ans+=x+z
        heappush(h,(-z,w))
        heappush(h2,(-x,y))
        using.remove((-z,w))
        using.add((x,y))
      else:
        heappush(h,(x,y))
        heappush(h2,(z,w))
    ans2.append(ans)
  print(*ans2)