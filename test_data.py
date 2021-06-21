import covidbr as cb
cb.logging.show_console = True
place = 'Petrolina PE'
data_pet = cb.data_from_city(place)
print(cb.create_painel(data_pet))
