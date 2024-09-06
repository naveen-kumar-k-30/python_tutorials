sq_list = list(map(lambda x: x * x, range(1, 11)))
print(sq_list)
sq1_list = [x*x for x in range(1,9)]
print(sq1_list)
sq2_list = [x*x for x in range(1,9) if x>4]
print(sq2_list)
sq3_list = [x*x if x>4  else 0 for x in range(1,9) ]
print(sq3_list)









