'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be 
truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed 
integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1 
and if the quotient is strictly less than -2^31, then return -2^31.

10
3
7
-3
2147483647
1
-2147483648
-1
'''

def is_neg(n:int) -> bool:
    if n < 0:
        return True
    elif n >= 0:
        return False

def is_pos(n:int) -> bool:
    if n >= 0:
        return True
    elif n < 0:
        return False


def div2(num1:int, num2:int):

    if is_pos(num1) and num2.
