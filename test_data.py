import covidbr as cb

cb.show_logs(True) #mostra os logs de cada processo

place = 'juazeiro BA'
data_city = cb.data_from_city(place)

print((data_city.dados['mortos']/data_city.dados['casos'])*100)