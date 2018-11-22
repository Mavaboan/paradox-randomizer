import random

#All countries added!!
#The different countrys numbers added automaticly and starts with 0
countries = [
    "Denmark", "Norway", "Finland", "UK", "USA", "Soviet Union", 
    "Poland",  "Ireland", "Sweden", "Germany", "France", "Spain", 
    "Italy", "Japan", "Iceland", "Lithuania", "Estonia", "Latvia",
    "Romania", "Yugoslavia", "Serbia", "Greece", "Albania", "Bulgaria",
    "Hungary", "Croatia", "Slovakia", "Luxemborg", "Belgium", "Netherlands",
    "Czechoslovakia", "Austria", "Portugal", "Switzerland", "Afghanistan",
    "Iraq", "Oman", "Iran", "Saudi Arabia", "Turkey", "Yemen", "Egypt",
    "Syria", "Lebonon", "Jordan", "Libya", "Australia", "New Zealand", 
    "Bhutan", "Tibet", "Nepal", "British Raj", "Philipines", "Siam",
    "China", "Guangxi Clique", "Peoples Republic of China", "Shanxi",
    "Xibei San Ma", "Sinkian", "Yunnan", "Mongolia", "Mengkukuo", "Tannu Tuva", 
    "Korea", "Liberia", "Ethiopia", "South Africa", "Canada", "Mexico",
    "Costa Rica", "El Salvadore", "Guatamala", "Honduras", "Nicaragua",
    "Panama", "Cuba", "Dominican Republic", "Haiti", "Brazil", "Argentina",
    "Chile", "Colombia", "Bolivia", "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela"
]

#!! Need hardcode the country flags into the code !!
#Finds out how many countries there are
country_amount = len(countries)
#Finds a random number between 0 and the amount of countries we have
random_number = random.randint(0,country_amount)
#Prints the name of a country from the list, based on the random number
print(countries[random_number])

#TODO - Add country flags