'''
Test script for demo push to git
'''

from secrets import token_hex

def test_token_hex(num:int):
    return token_hex(num)

if __name__=="__main__":
    print(test_token_hex(99))