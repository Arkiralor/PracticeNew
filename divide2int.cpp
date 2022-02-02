 /*
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
 */
 
 #include<iostream>

using namespace std;

long int divide(int d1, int d2) 
    {
        long int q = 0;
        if (d1 > 2147483647)
        {
            return 2147483647;
        }
        else if (d1 < -2147483648)
        {
            return 2147483647;
        }
        
        if (d1>0 && d2>0) // 10 3
        {
            while (d1 >= 0)
            {
                d1 = d1 - d2;
                q++;
                if (q == -2147483648)
                {
                    return q;
                }
                else if (q == 2147483647)
                {
                    return q;
                }
            }
            return q-1;
        }
        else if (d1>0 && d2<0) // 10 -3
        {
            while (d1 >= 0)
            {
                d1 = d1 + d2;
                q--;
                if (q == -2147483648)
                {
                    return q;
                }
                else if (q == 2147483647)
                {
                    return q;
                }
            }
            return q+1;
        }
        else if (d1<0 && d2>0) // -10 3
        {
            while (d1 <= 0)
            {
                d1 = d1 + d2;
                q--;
                if (q == -2147483648)
                {
                    return q;
                }
                else if (q == 2147483647)
                {
                    return q;
                }
            }
            return q+1;
        }
        else if (d1<0 && d2<0) // -10 -3
        {
            while (d1 <= 0)
            {
                d1 = d1 - d2;
                q++;
                if (q == -2147483648)
                {
                    return q;
                }
                else if (q == 2147483647)
                {
                    return q;
                }
            }
            return q-1;
        }
        return 0;
    }

int main()
{
    int a, b;
    cin>> a >> b;
    long int res = divide(a, b);
    cout<<res;
    return 0;
}

