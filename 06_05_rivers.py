rivers = {'Nile': 'Egypt', 'Amazon': 'Brazil',
          'Yangtze': 'China'}

#Sentences about the rivers
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

#Names of each river
print("Rivers included in the dictionary:")

for river in rivers.keys():
    print(river)

#Names of each country
print("Countries included in the dictionary:")

for country in rivers.values():
    print(country)