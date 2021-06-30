import covidbr as cb
cb.show_console(True)
cb.log('testing the painel covid plot')

data_pet = cb.data_from_city('Petrolina PE')
cb.painel_covid(data_pet)
