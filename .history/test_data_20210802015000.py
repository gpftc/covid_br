import covidbr as cb
cb.show_console(True)

place = 'paulo afonso BA'
data_pet = cb.data_from_city(place)
print(data_pet)
#print(cb.create_painel(data_pet))
