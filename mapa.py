import folium

# cria o mapa #
mapa = folium.Map(
    location=[-23.5500093493433984, -46.341472592547],
    tiles='Stamen Terrain',  # estilo do mapa #
    zoom_start=16
)

# adiciona o mercado no mapa #
folium.Marker(
    [-23.5500093493433984, -46.341472592547],
    popup='<i> Praça da Sé </i>',
    tooltip='Click aqui!'
).add_to(mapa)

# Salvando html do mapa #
mapa.save(r'.\mapa.html')
