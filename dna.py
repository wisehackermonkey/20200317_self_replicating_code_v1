# dna like replication using practical file based quines
# created by oran c
# 20200317

from time import sleep

dna = "1"

lifespan = 0

with open(__file__) as f:
    sleep(int(dna))
    plant_code = "\n".join(f.read().split("\n")[1:])
    plant_code