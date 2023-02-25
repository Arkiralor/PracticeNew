'''
Multiply all values in list except for the current value:
[1, 2, -1, 1, 2]
    => [-4, -2, 4, 4, -2]
'''
import numpy as np

inp_ls = [
    1, 
    2, 
    # 0, 
    -1, 
    # 0, 
    1, 
    2
]
op_li = []

x = len(inp_ls)
# prod = np.prod(inp_ls)
for i in range(x):
    prod_01 = 1
    prod_02 = 1
    prev_slice = inp_ls[0:i]
    next_slice = inp_ls[i+1:]
    for item in prev_slice:
        prod_01 = prod_01*item
    for jitem in next_slice:
        prod_02 = prod_02*jitem


    final_prod = prod_01 * prod_02
    try:
        op_li.append(final_prod)
    except Exception as ex:
        print(f"Error: {ex}")


print(f"Output: {op_li}")
