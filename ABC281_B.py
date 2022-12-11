import io
import sys

_INPUT = """\
6
Q142857Z
AB912278C
X900000
K012345K
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  if len(S)!=8: print('No')
  else:
    s,g=S[0],S[-1]
    if ord(s)<ord('A') or ord(s)>ord('Z') or ord(g)<ord('A') or ord(g)>ord('Z'):
      print('No')
    else:
      S=S[1:-1]
      ans='Yes'
      for i in range(6):
        if ord('A')<=ord(S[i])<=ord('Z'): ans='No'
      if ans=='Yes':
        if int(S)<100000: ans='No'
      print(ans)