import dataanalise as da
import plotly.express as px

data = da.lerdados()

data['somaedu'] = data['idebanosiniciais'] + data['idebanosfinais']

print(data.dtypes)

#print(data.sort_values(by=['somaedu'], ascending=False))
