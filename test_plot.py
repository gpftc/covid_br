#import covidbr as cb
import covidbr as cb

#print(cb.logger.__log__)
cb.logging.show_console = True
cb.logging.log('oi')


############## teste da biblioteca principal #############
city = 'Petrolina PE'
data_covid = cb.data_from_city(city)

#plotando
cb.plot_media_cases(data=data_covid,limit_period=40)

