'''
3.0 4.0 2.0 0.0 4.0 0.0
3.0 4.0 2.0 90.0 4.0 0.0
6.0 8.0 2.14 75.2 9.58 114.3
3.0 4.0 5.0 0.0 5.0 90.0
'''
import math
import sys; sys.stdin=open('./20230912_b1798_원뿔좌표계상의 거리.py', encoding='utf-8'); qwfasd = input();

r, h, d1, A1, d2, A2 = map(float,input().split())

r2 = ((r**2) + (h**2))**.5

theta = 360*r/r2

aa = abs(A2 - A1)
if aa > 180:
    aa = 360-aa

