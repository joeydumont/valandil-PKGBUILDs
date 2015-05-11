from PyGMO import *
prob = problem.schwefel(dim = 50)
algo = algorithm.de(gen = 500)
archi = archipelago(algo,prob,8,20)
print( min([isl.population.champion.f for isl in archi]))
archi.evolve(10)
print (min([isl.population.champion.f for isl in archi]))
