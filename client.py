from utils import *
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
import glob

class Corona:

    def _draw_a_graph(self, country, dates, confirmed, deaths, recovered, percentage1, percentage2, percentage3):
        print(f"Drawing a graph for {country}!")
        plt.grid()
        plt.plot(dates, confirmed, "-b", label='confirmed')
        plt.plot(dates, deaths, "-r", label='deaths')
        plt.plot(dates, recovered, "-g", label='recovered')
        plt.legend(loc='upper left')
        plt.xlabel('Date')
        for x, y, z, p in zip(dates, confirmed, deaths, recovered):
            labely = y
            plt.annotate(labely, (x, y), textcoords='offset points', xytext=(0, 30), ha='center', size='7',
                         color='blue')
            labelz = z
            plt.annotate(labelz, (x, z), textcoords='offset points', xytext=(0, 20), ha='center', size='7', color='red')
            labelp = p
            plt.annotate(labelp, (x, p), textcoords='offset points', xytext=(0, 10), ha='center', size='7', color='green')
        plt.ylabel('Nr of individuals')
        plt.title(f'Development of COVID-19 virus in {country}')
        plt.gca().margins(x=0)
        plt.gcf().canvas.draw()
        tl = plt.gca().get_xticklabels()
        maxsize = max([t.get_window_extent().width for t in tl])
        m = 0.2
        s = maxsize / plt.gcf().dpi * 150 + 2 * m
        margin = m / plt.gcf().get_size_inches()[0]
        plt.gcf().subplots_adjust(left=margin, right=1. - margin)
        plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
        plt.annotate(percentage1, (0.1,900), textcoords='offset points', xytext=(dates[0], confirmed[0]), size='8')
        plt.annotate(percentage2, (0.1,950), textcoords='offset points', xytext=(dates[0], confirmed[0]), size='8')
        plt.annotate(percentage3, (0.1,1000), textcoords='offset points', xytext=(dates[0], confirmed[0]), size='8')
        plt.xticks(rotation=45, fontsize=6)
        filename = f'graph{datetime.datetime.now().timestamp()}.png'
        print(filename)
        return(plt.savefig(f'static/graphs/{filename}', dpi=300))

    def _create_plot_data(self, country):
        print(f"Creating plot data for {country}!")
        dates, confirmed, deaths, recovered = create_country_stats(country)
        percentage1 = calculate_percentage_of_deaths_relative_to_infected(deaths[-1], confirmed[-1])
        percentage2 = calculate_percentage_of_recovered_relative_to_infected(recovered[-1], confirmed[-1])
        percentage3 = biggest_change_global()
        return(self._draw_a_graph(country,dates,confirmed,deaths,recovered,percentage1,percentage2,percentage3))

    def _request_user_input(self):
        country = input("Enter a country you wish to plot for: ")
        return self._create_plot_data(country)

    def plot(self, country=None):
        if country is None:
            return self._request_user_input()
        else:
            print(f"Received {country} as country!")
            return self._create_plot_data(country=country)