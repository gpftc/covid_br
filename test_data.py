import covidbr as cb

cb.show_logs(True) #mostra os logs de cada processo

place = 'juazeiro BA'
data_city = cb.data_from_city(place)

cb.plot_media_cases(data=data_city,limit_period=365)

