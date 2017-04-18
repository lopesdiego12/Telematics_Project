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
crash = ['S', 'N']

# Geracao fixa de host e .com e .br
user = ["amin", "andrew", "anthony", "apolo", "benjamin", "bryan", "cau", "caleb", "cssio", "ciro", "conrado", "dante", "derek", "dionsio", "elieser", "eloy", "elton", "enrico", "enzo", "erik", "estevo", "ettore", "fausto", "fauzer", "frederico", "gaspar", "gregory", "ian", "issac", "heitor", "henri", "herton", "hugo", "caro", "talo", "joaquim", "jonas", "kaique", "keid", "leon", "levi", "lorenzo", "lucca", "luigi", "martin", "max", "nathan", "nicolas", "olavo", "otto", "patrick", "romero", "ryan", "thales", "theo", "toms", "umberto", "vicente", "zya", "agatha", "agnes", "alba", "alexa", "analu", "betina", "brenda", "cassiane", "catarina", "ceclia", "chiara", "daisy", "dalila", "doris", "dinor", "ellen", "elo", "evelyn", "ester", "fabola", "fabrcia", "fany", "fiona", "graziela", "helosa", "hilda", "ins", "ingrid", "inara", "iris", "isis", "ivna", "jamille", "joyce", "juliete", "jussara", "kate", "kamilly", "knia", "kristen", "lavnia", "lolita", "lorraine", "mait", "mal", "marjorie", "nayla", "nina", "paola", "pietra", "rebeca", "samanta", "samila", "samira", "sibele", "stella", "suzete", "thauany", "valentina", "vivian", "yanna"]
TLDS = ['.com', '.br']
host = ['@gmail', '@hotmail']
now = datetime.datetime.now()

#All Functions

# Generate fake e-mail addresses.
def address_generator():
    return user[randint(0, len(user)-1)] + host[randint(0,len(host)-1)] + choice(TLDS)

result = []
sep = []
for i in range(0, 12):
    #CSV VARIABLES

    # ID DO CARRO
    idcarro = str(random.randrange(1, 1000, 2))

    # AGE ENTRE 18 E 80
    age = str(random.randrange(18, 80, 2))

    #DATE
    date = now.strftime("%Y-%m-%d")

    # VELOCIDADE DO CARRO
    avgvelocity = str(random.randrange(0, 250, 2))

    #Genero
    genero = random.choice(gender)

    #Email
    if __name__ == '__main__':
        email = str(address_generator())

        # KM
        km = str(random.randrange(0, 8000, 2))

        #MARCHA
        marcha = random.choice(marcha)
        
		#Acidente
        acidente = random.choice(crash)
        
		#Rodovia
        rodovia = random.choice(road)

        #Longitude
        longitude = str(random.randrange(18, 80, 2))

        #Latitude
        latitude = str(random.randrange(18, 80, 2))

        result.append([idcarro, age, date, avgvelocity, email, genero, acidente, km, marcha, rodovia, longitude, latitude])
        with open ('dataset.csv','w') as f:
            wtr = csv.writer(f, delimiter ='\n',quoting=csv.QUOTE_MINIMAL)
            wtr.writerow(result)
        f.close()  