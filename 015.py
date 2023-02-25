"""
Script to multiply two hex sequences produced by `secrets.token_hex`
"""

from secrets import token_hex

def main():
    token_1 = int(f"{token_hex(16)}", 16) ## We convert the two str objects returned by token_hex to 16-digit integer objects.
    token_2 = int(f"{token_hex(16)}", 16) ## We do this because we cannot multiply two strings.

    print(f"Token 1:\t{hex(token_1)}\nToken 2:\t{hex(token_2)}")

    comp_token = hex(token_1*token_2)

    print(f"Compound Token:\t{comp_token}")

if __name__=="__main__":
    main()