import requests
from collections import Counter

# population_url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json"
url = "https://pomber.github.io/covid19/timeseries.json"
data = requests.get(url).json()
countries = sorted([country for country in data])
# population = requests.get(population_url).json()

def get_countries():
    return countries

def get_country_data(country):

    return data[f"{country}"]

#def get_population(country):
#    data = list(filter(lambda elem: elem['country'] == country, population))
#    return data

def create_country_stats(country):
    dates = []
    confirmed = []
    deaths = []
    recovered = []
    for date in get_country_data(country):
        dates.append(date['date'])
        confirmed.append(date['confirmed'])
        deaths.append(date['deaths'])
        recovered.append(date['recovered'])
    return(dates, confirmed, deaths, recovered)

def create_confirmed_stats(country):
    confirmed = []
    for date in get_country_data(country):
        confirmed.append(date['confirmed'])
    return(confirmed)

def calculate_percentage_of_deaths_relative_to_infected(deaths, confirmed):
    percentage = round((deaths/confirmed)*100, 1)
    return(f'Percentage of deaths relative to infected: {percentage}%')

def calculate_percentage_of_recovered_relative_to_infected(recovered, confirmed):
    percentage = round((recovered/confirmed)*100, 1)
    return(f'Percentage of recovered relative to infected: {percentage}%')

def biggest_change_in_infected_relative_to_previous_statistics(newly_infected, previously_infected):
    percentage = round((newly_infected/previously_infected)*100,1) if previously_infected else 0
    return percentage

def biggest_change_global():
    percentage_dict = {}
    for country in get_countries():
        confirmed = create_confirmed_stats(country)
        if confirmed[-1]>100:
            percentage_dict[country] = biggest_change_in_infected_relative_to_previous_statistics((confirmed[-1]-confirmed[-2]), confirmed[-2])
    country = max(percentage_dict, key=percentage_dict.get)
    max_value = percentage_dict[country]
    return(f'Biggest change in infected relative to previous day in {country}: {max_value}%')
