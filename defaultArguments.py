# def net_prixce(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)
#

import time

def count (end, start = 0):
    for x in range (start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)