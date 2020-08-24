import requests

population_url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json"
population = requests.get(population_url).json()

def get_population(country):
    for dict in population:
        print(dict)
        if dict['country'] == country:
            return(dict)

print(get_population('US'))