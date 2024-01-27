import random
# from random import randint
import datetime

x = datetime.datetime.now()
print(x)

number1 = round(random.random(), 2)
number2 = round(random.random(), 2)
number3 = round(random.uniform(1.0, 8.0), 2)
number4 = round(random.uniform(1.0, 50.0), 2)
number5 = round(random.uniform(9.0, -100.0), 2)
number6 = round(random.uniform(1.0, -30.0), 2)
number6 = round(random.uniform(1.0, -60.0), 2)
number7 = round(random.uniform(1.0, 100.0), 2)
number8 = round(random.uniform(1.0, 100.0), 2)



randomiser = number1 * 100
rounded  = round(randomiser)
print("rounded", rounded)





randomiser = [number1, number2, number3, number4, number5, number6, number7, number8]
random.shuffle(randomiser)
print(*randomiser, sep='\n')
print(percent)

randomiser = number1 * 100
rounded  = round(randomiser)
print("rounded", rounded)


