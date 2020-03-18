# dna li2e replication using practical file based quines
# created by oran c
# 20200317

from time import sleep, time
from random import randint

lifespan = 0

with open(__file__) as f:
    sleep(int(dna))
    plant_code = "\n".join(f.read().split("\n")[1:])
    t = list(plant_code)
    t[8] = str(randint(0,10))
    plant_code = "".join(t)
    print(plant_code)


    file_name = __file__[:-3] + "_" + str(int(dna) + 1) + ".py"
    print(file_name)

    # f.write(plant_code)
    with open(file_name,"w") as new_f:
        new_f.write(plant_code)