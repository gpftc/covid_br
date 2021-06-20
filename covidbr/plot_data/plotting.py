import matplotlib.pyplot as plt
from matplotlib import ticker
from covidbr.log import date_base
from covidbr.get_data import data_from_city as dc
from covidbr.statistical_functions.bases import mov_average
import numpy as np


############### plotting media in the maxim period limited ###################
def plot_media_cases(data:dc,limit_period:int=0,title:str=None,show:bool=True,path_dir:str=f'data/'):
    '''
    sumary:

    '''
    #verification of data input is a data_from_city classtype
    if(data.type=='covid_dataframe'):
        pass
    else:
        raise Exception(f'[{date_base()}] Error! dataFrame is not a covid_br.get_data_covid')

    if limit_period:
        dados_bar = data.dados[-limit_period:]
        casos_diarios = data.dados['casos_diarios']
        media = mov_average(casos_diarios,7)
        media = media[-limit_period:]
        print('0 == False')
    else:
        dados_bar = data.dados
        casos_diarios = data.dados['casos_diarios']
        media = mov_average(casos_diarios,7)
        media_casos = media
        print('oks')

        limit_period = len(dados_bar.index)
    dados = data.dados
    city = data.city
    state = data.state

    ax = dados_bar.plot(x='date',y='casos_diarios',kind='bar',color='black')
    print(f'encontrando a média móvel de casos confirmados em {city}-{state}...')
    
    #media = calcSma(casos_diarios,7)
    media_casos = media
    #print((media.max))
    plt.ylim((0,max(casos_diarios[-limit_period:])+10))
    date = dados_bar['date']
    plt.plot(date,media,label='media móvel',c='red')
    #plt.grid()

    ticklabels = ['']*len(dados_bar.index)
    ticklabels[::int(limit_period/10)] = dados_bar['date'][::int(limit_period/10)]
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
    plt.gcf().autofmt_xdate()

    plt.legend()
    if title:
        plt.tile(f'{title}')
    elif(title=='pt-br'):
        plt.title(f'casos diarios em covid-19 em {city}-{state} nos últimos {limit_period} dias')
    if path_dir:
        plt.savefig(f'{path_dir}{city}_plot_cases_{abs(limit_period)}.jpg',dpi=900)
    if(show):
        plt.show()

    plt_casos = plt

    return plt_casos



################ tools for plotting of deaths data period limited ############### 
def plot_media_deaths(data:dc,limit_period:int=0,title:str=None,show:bool=True,path_dir:str='data/'):
    '''
    sumary:

    '''
    #verification of data input is a data_from_city classtype
    if(data.type=='covid_dataframe'):
        pass
    else:
        raise Exception(f'[{date_base()}] Error! dataFrame is not a covid_br.get_data_covid')

    if limit_period:
        dados_bar = data.dados[-limit_period:]
        deaths_day = data.dados['mortes_diarias']
        media = mov_average(deaths_day,7)
        media_casos = media
        media = media[-limit_period:]
        print('0 == False')
    else:
        dados_bar = data.dados
        deaths_day = data.dados['mortes_diarias']
        media = mov_average(deaths_day,7)
        media_casos = media
        print('oks')

        limit_period = len(dados_bar.index)
    dados = data.dados
    city = data.city
    state = data.state

    ax = dados_bar.plot(x='date',y='mortes_diarias',kind='bar',color='black')
    date = dados_bar['date']
    plt.plot(date,media,label='media movel',c='red')

    ticklabels = ['']*len(dados_bar.index)
    ticklabels[::int(limit_period/10)] = dados_bar['date'][::int(limit_period/10)]
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
    plt.gcf().autofmt_xdate()
    plt.grid()
    plt.legend()

    if path_dir:
        plt.savefig(f'{path_dir}{city}_plot_deaths_{abs(limit_period)}.jpg',dpi=900)
    if(show):
        plt.show()

    plt_casos = plt
    return plt_casos
