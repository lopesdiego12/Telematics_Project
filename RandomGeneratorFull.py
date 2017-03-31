import csv
import datetime
import random
from itertools import islice
from random import choice, randint
from string import ascii_lowercase

#Fixed variables
marcha = ['S', 'N']
gender = ['F', 'M']
road = ['S', 'N']
# Geracao fixa de host e .com e .br
TLDS = ('com'' br').split()
HOST = ('gmail'' hotmail').split()


now = datetime.datetime.now()
# define current time when file is executed

result = []
for i in range(0,12):
    #CSV VARIABLES
    # ID DO CARRO
    idcarro = str(random.randrange(1, 1000, 2))
    # AGE ENTRE 18 E 80
    age = str(random.randrange(18, 80, 2))
    #DATE
    date = now.strftime("%Y-%m-%d %H:%M")
    # VELOCIDADE DO CARRO
    avgvelocity = str(random.randrange(0, 250, 2))
    #Genero
    genero = random.choice(gender)
    # KM
    km = str(random.randrange(0, 8000, 2))
    #MARCHA
    marcha = random.choice(marcha)
    #Rodovia
    rodovia = random.choice(road)
    #Longitude
    longitude = str(random.randrange(18, 80, 2))
    #Latitude
    latitude = str(random.randrange(18, 80, 2))
    
    result.append([idcarro, age, date, avgvelocity, km, marcha, rodovia, longitude, latitude])
    with open ('dataset.csv','w') as f:
        wtr = csv.writer(f)
        wtr.writerow(result)
    f.close()