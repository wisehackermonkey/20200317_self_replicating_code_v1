#%%
# var = 'print("var = " + var + " eval(val)")'
# eval(var)

import random
ASCII_NUMBER_A = 97


rand_char = chr(random.randint(ASCII_NUMBER_A,ASCII_NUMBER_A+26))

print(rand_char)
mutation = f"""
try:
    {rand_char}
except:
    print("error")
"""

print(__file__)
with open(__file__) as f:
    source = "\n".join(f.read().split("\n")[1:])
    index = random.randint(0,len(source))
    print(f"index {source[index:index+5]}")
    # elabrate way to change one character randomly in an array
    source_mutated = source[:index] + rand_char + source[index+1:]
    print(source_mutated + mutation)
# %%
