from client import Corona
import datetime

corona = Corona()
corona.generate_plot('Serbia')
corona.plt.savefig(f'static/graphs/graph{datetime.datetime.now().timestamp()}.png', dpi=300)