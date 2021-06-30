#import covidbr as cb
import covidbr as cb
from covidbr import create_painel
#print(cb.logger.__log__)
cb.logging.show_console(True)
cb.logging.log('oi')
log = cb.logging.log
import matplotlib.pyplot as plt

############## teste da biblioteca principal #############
city = 'Petrolina PE'
data_covid = cb.data_from_city(city)

#plotando
#cb.plot_media_cases(data=data_covid,limit_period=60,
#color_bar='#4ea286',color_line='black')
cb.logging.show_console = True
log = cb.logging.log
city = 'Juazeiro BA'
limit_period = 30
data_city_covid = cb.data_from_city(city)
cb.create_painel(data_city_covid,limit_period=limit_period)

log(f'publicando media movel de casos nos útimos {limit_period} dias')
plt = cb.plot_media_cases(data=data_city_covid, show=False,
                          color_bar='#4ea286', color_line='black', limit_period=limit_period)
plt.title(f'média móvel de casos da covid-19 na cidade de {city} em {limit_period}')
plt.grid()
path_img_cases = f'plot_media_cases_{city[:3]}.png'
plt.savefig(path_img_cases, dpi=800)
#bot.upload_photo(photo=path_img_cases,caption=f'plotagem de casos da covid-19 nos últimos {limit_period} dias na cidade de {city} {data_city_covid.date_upload} \n#petrolina #covid #data #python')

log(f'publicando media movel de mortes nos últimos {limit_period} dias')
plt = cb.plot_media_deaths(data=data_city_covid, show=False,
                          color_bar='#8e43b5', color_line='black', limit_period=limit_period)
plt.title(f'média móvel de mortes da covid-19 na cidade de {city} em {limit_period}')
#plt.grid()
path_img_cases = f'plot_media_deaths_{city[:3]}.png'
plt.savefig(path_img_cases, dpi=800)
#bot.upload_photo(photo=path_img_cases,caption=f'plotagem dos números de mortes da covid-19 nos últimos {limit_period} dias na cidade de {city} {data_city_covid.date_upload} \n#petrolina #covid #data #python')
log('feito!')