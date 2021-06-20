import covidbr as cb
cb.logging.show_console = True
place = 'Petrolina PE'
data_pet = cb.data_from_city(place)
print(data_pet.create_painel())
