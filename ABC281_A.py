import io
import sys

_INPUT = """\
6
3
22
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  for i in range(N+1):
    print(N-i)