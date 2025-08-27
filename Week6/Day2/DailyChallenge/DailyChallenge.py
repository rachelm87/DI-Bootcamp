import psycopg2
import requests
import json
import os
import random
dir_path = os.path.dirname(os.path.realpath(__file__))


#code for the connection
connection = psycopg2.connect(database = 'countries',
    user = 'rachel',
    password = 'rachel',
    host = 'localhost',
    port = '5432')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS exercise(
               country_id SERIAL PRIMARY KEY,
               country_name VARCHAR (200) NOT NULL,
               capital VARCHAR (200),
               flag_png VARCHAR(200),
               subregion VARCHAR (200),
               population INTEGER NOT NULL)''')

connection.commit()

print('connection successfully made. Table was created')

# get API and create JSON file

#due to connection issues, we need to insert a list of parameters, which require knowing what keys are in the API. 
#therefore, we ran a test - with France. The list of keys we want need to match the homework instruction. 

# response = requests.get("https://restcountries.com/v3.1/name/france", timeout=20) 
# response.raise_for_status()
# data = response.json()            # list with one or a few matches
# first = data[0]
# print(sorted(first.keys()))

#now that we know this, we can go ahead and insert this into the proper actual formula

url = 'https://restcountries.com/v3.1/all'
params = {"fields": "name,capital,flags,subregion,population"} #i inserted based on the 'test' with France.

response = requests.get(url, params, timeout=20)

##chatgpt recommends i do this to make sure no issues - it shows what it pulled in the terminal
print("Status:", response.status_code, "URL:", response.url) 
response.raise_for_status() 

#the next two lines pull the API data into the json file
data = response.json()

with open(f'{dir_path}/countries.json', "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)


#get 10 random
results = random.sample(data, 10)
print(results)

#clean up data
def clean (country):
    country_name = country["name"]["common"]
    try:
        capital_list = country["capital"]
        capital = capital_list[0] if capital_list else None
        if '\'' in capital:
            capital = capital.replace('\'', '`')   
    except:
        capital = None
    flag_png = country["flags"]["png"]
    subregion = country["subregion"]
    population = country["population"]
    return country_name, capital, flag_png, subregion, population

#transfer data

for country in results:
    country_name, capital, flag_png, subregion, population = clean(country)
    cursor.execute(f'''INSERT INTO exercise (country_name, capital, flag_png, subregion, population)
                VALUES ('{country_name}', '{capital}', '{flag_png}', '{subregion}', '{population}')''')
connection.commit()

print('table successfully populated')

# see results!!
cursor.execute("SELECT * FROM countries")

rows = cursor.fetchall()

for row in rows:
    print(row)

#close it
cursor.close()
connection.close()