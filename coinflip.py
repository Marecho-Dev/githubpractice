import random
coinflip = []

for x in range(36):
	cointoss = random.randrange(0,2)
	coinflip.append(cointoss)
# 	# if cointoss == 0:
# 	# 	coinflip.append("tails")
# 	# else:
# 	# 	coinflip.append("heads")
# 	# # coinflip.append(random.randrange(0,2))

print(coinflip)

size = 8
rows = 3
columns = 2
position = (3,3)
maplist =	 [[0,0,0,0,0],
			  [0,0,0,0,0],
			  [0,0,1,0,0],
			  [0,0,0,0,0],
			  [0,0,0,0,0]]

print(maplist)