import itertools
coins = (200,100,50,20,10,5,2,1)
possibles = []
possibles.append(itertools.combinations_with_replacement(coins, 5))
print possibles
