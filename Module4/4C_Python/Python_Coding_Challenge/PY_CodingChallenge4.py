# print a table containing multiplication tables


for i in range(1, 12):
    for j in range(1, 12):
        res = i * j
        print(res, end="\t")
    print()
