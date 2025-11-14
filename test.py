import random


x = random.getrandbits(12)  # 8 losowych bitów (0–255)




seq = random.getrandbits(12)       # 12-bit sequence number
frag = random.getrandbits(4)       # 4-bit fragment number
print(bin(seq),bin(frag))
sc_field = (seq << 4) | frag


print(bin(sc_field))