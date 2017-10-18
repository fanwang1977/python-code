import random
population = [0 for i in range(10000)]
for i in range(1000):
    population[i] = 1
for iterator in range(10):
    sample = [0 for i in range(100)]
    for i in range(100):
        sample[i] = population[random.randrange(10000)]
    count = 0
    for i in range(100):
        count += sample[i]
    print('%.2f' % (float(count)/100))
