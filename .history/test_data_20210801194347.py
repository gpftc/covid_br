import covidbr as cb
cb.show_console(True)

place = 'Petrolina PE'
data_pet = cb.get_data_city(place)
print(data_pet)
#print(cb.create_painel(data_pet))
