import covidbr as cb
cb.show_console(True)

place = 'juazeiro BA'
data_pet = cb.data_from_city(place)
print(data_pet)
cb.painel_covid(data_pet,limit_period=30)
