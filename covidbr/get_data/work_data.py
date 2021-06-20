#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from covidbr.io_api import login_io
from covidbr.log import log
from covidbr.statistical_functions.bases import mov_average, per_size,percent_basic

import pandas as pd
import numpy as np
import os
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import Image


#api_io = login_io.API_io

############### tratamento de dados ############
class data_from_city:
    def __init__(self,city_state:str):
        self.type = 'covid_dataframe'
        self.city,self.state = tuple(city_state.split())
        self.api_io = login_io.API_io()
        self.data = self.api_io.get_data_covid_from_city(city_and_state=city_state)

        if(not os.path.isdir('data')):
            os.system('mkdir data')
            self._path_cache = 'data/'
        else:
            self._path_cache = 'data/'
        
        log('organizando dados do DataFrame...')
        self.dados_dict = self.miner_data(self.data)
        
        log('construindo um novo DataFrame...')
        self.dados = pd.DataFrame(self.dados_dict,index=self.dados_dict['date'])
        log('DataFrame construido com sucesso!')
        log('criando excel com os dados...')
        self.dados.to_excel(f'{self._path_cache}dados_{self.city}_{self.state}.xlsx')
        print('Excel criado com sucesso')
        print('dados ok!')
        
        log('mining statistical data...')
        self.mining_statistical_data(limit_period=15)
        log('statistical data mined! ')
    
    
    
    def mining_statistical_data(self,limit_period:int=15):
        size = limit_period
        #### deaths ####
        ## making string ##
        all_deaths_string = list(str(self.mortes[-1]))
        if len(all_deaths_string) >= 4:
            all_deaths_string.insert(-3,'.')
        print(all_deaths_string)
        self.all_deaths_string = ''.join(all_deaths_string)
        ## others estatistic of this ##
        self.deaths_movel = mov_average(self.mortes_diarias,7)
        percent_deaths = per_size(self.deaths_movel,size)
        self.percent_deaths = round(percent_deaths,2)
        self.percent_all_deaths = percent_basic(self.mortes,size)
        param_per_deaths = 'up' if(percent_deaths > 0) else 'down'
        self.deaths_24h = self.mortes_diarias[-1]
        self.deaths_on_period = sum(self.mortes_diarias[-size:])
        
        ### cases ###
        ## making string for fluctuate point ##
        all_cases_string = list(str(self.casos[-1]))
        if len(all_cases_string) >= 4:
            all_cases_string.insert(-3,'.')
        print(all_cases_string)
        self.all_cases_string = ''.join(all_cases_string)
        ## others estimates of this ##
        self.cases_movel = mov_average(self.casos_diarios,7)
        percent_cases = per_size(self.cases_movel,size)
        self.percent_cases = round(percent_cases,2)
        self.percent_all_cases = percent_basic(self.casos,size) 
        param_per_cases = 'up' if(percent_cases > 0) else 'down'
        self.cases_24h = self.casos_diarios[-1]
        self.deaths_on_period = sum(self.mortes_diarias[-size:])
        
    


    def miner_data(self,data):
        self.casos = np.array(self.data['last_available_confirmed'][::-1])
        self.mortes = np.array(self.data['last_available_deaths'][::-1])
        self.casos_diarios = np.array(self.data['new_confirmed'][::-1])
        self.mortes_diarias = np.array(self.data['new_deaths'][::-1])
        self.population = np.array(self.data['estimated_population'][::-1])

        meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
        date = self.data['date'][::-1]
        years = [i[4:] for i in date]
        self.date = [i.split('-') for i in date]
        print(self.date)
        self.date = [('/').join([i[2],meses[int(i[1])-1],i[0]]) for i in self.date]
        dados = {'casos':np.array(self.casos),
            'mortos':np.array(self.mortes),
            'mortes_diarias':abs(np.array(self.mortes_diarias)),
            'casos_diarios':abs(np.array(self.casos_diarios)),
            'population':np.array(self.population),
            'date':self.date}
        log('dados do DataFrame organizadas!')
        return dados
        #file_name_data = api_io.file_data_excel



    def get_media_movel_deaths(self,smaPeriod:int):
        j = next(i for i, x in enumerate(abs(np.array(self.mortes_diarias))) if x is not None)
        data = abs(np.array(self.mortes_diarias))
        our_range = range(len(data))[j + smaPeriod - 1:]
        empty_list = [None] * (j + smaPeriod - 1)
        sub_result = [np.mean(data[i - smaPeriod + 1: i + 1]) for i in our_range]

        self.media_movel_deaths = np.array(empty_list + sub_result)
        return self.media_movel_deaths



    def get_media_movel_cases(self,smaPeriod:int):
        j = next(i for i, x in enumerate(abs(np.array(self.casos_diarios))) if x is not None)
        data = abs(np.array(self.mortes_diarias))
        our_range = range(len(data))[j + smaPeriod - 1:]
        empty_list = [None] * (j + smaPeriod - 1)
        sub_result = [np.mean(data[i - smaPeriod + 1: i + 1]) for i in our_range]

        self.media_movel_cases = np.array(empty_list + sub_result)
        return self.media_movel_cases


    def create_painel(self,limit_period=15):
        size = limit_period

        img = Image.open("painel_covid.jpg").convert('RGB')
        draw = ImageDraw.Draw(img)
        ## adding date update in the image ##
        font = ImageFont.truetype("arial_unicode.ttf",18)
        draw.text((150,150),self.date[-1],'#8b9bae',font=font)
        ## adding the name city ##
        font = ImageFont.truetype("arial_unicode.ttf",18)
        draw.text((35,200),f'Cidade: {self.city} {self.state}','#8b9bae',font)
        
        ### creating the painel imagefor deaths ###
        font = ImageFont.truetype("arial_unicode.ttf", 40)
        draw.text((460, 320),self.all_deaths_string,'#8e43b5',font=font)
        ## 24h ##
        font = ImageFont.truetype("arial_unicode.ttf", 20)
        draw.text((700, 245),' 24h','#8e43b5',font=font)
        font = ImageFont.truetype("arial_unicode.ttf", 35)
        draw.text((700, 265),f' {self.mortes_diarias[-1]}','#8e43b5',font=font)
        ## 15 days ##
        font = ImageFont.truetype("arial_unicode.ttf", 20)
        draw.text((700, 320),f'{size} dias','#8e43b5',font=font)
        font = ImageFont.truetype("arial_unicode.ttf", 35)
        sum_deaths_period = list(f'{sum(self.mortes_diarias[-size:])}')
        if len(sum_deaths_period) >= 4:
            sum_deaths_period.insert(-3,'.')
        sum_deaths_period=''.join(sum_deaths_period)
        draw.text((700, 340),f' {sum_deaths_period}','#8e43b5',font=font)
        ## percent variation ##
        font = ImageFont.truetype("arial_unicode.ttf", 20)
        #font=ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 16)
        draw.text((680, 400),'variância móvel','#8e43b5',font=font)
        font = ImageFont.truetype("arial_unicode.ttf", 35)
        draw.text((690, 420),f'{self.percent_deaths}%','#8e43b5',font=font)
        
         ### creating the painel image for cases ###
        font = ImageFont.truetype("arial_unicode.ttf", 40)
        draw.text((60, 320),self.all_cases_string,'#4ea286',font=font)
        ## 24h ##
        font = ImageFont.truetype("arial_unicode.ttf", 20)
        draw.text((290, 245),' 24h','#4ea286',font=font)
        font = ImageFont.truetype("arial_unicode.ttf", 35)
        draw.text((290, 265),f'{self.casos_diarios[-1]}','#4ea286',font=font)
        ## 15 days ##
        font = ImageFont.truetype("arial_unicode.ttf", 20)
        draw.text((290, 320),f' {size} dias','#4ea286',font=font)
        font = ImageFont.truetype("arial_unicode.ttf", 35)
        sum_cases_period = list(f'{sum(self.casos_diarios[-size:])}')
        if len(sum_cases_period) >= 4:
            sum_cases_period.insert(-3,'.')
        sum_cases_period=''.join(sum_cases_period)
        draw.text((290, 340),sum_cases_period,'#4ea286',font=font)
        ## percent variation ##
        font = ImageFont.truetype("arial_unicode.ttf", 20)
        #font=ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 16)
        draw.text((260, 400),'variância móvel','#4ea286',font=font)
        font = ImageFont.truetype("arial_unicode.ttf", 35)
        draw.text((290, 420),f'{self.percent_cases}%','#4ea286',font=font)

        
        img.save('sample-out.jpg')
        
        return f'''
                    "date_update": {self.date[-1]},
                    "all_confirmeds": {self.casos[-1]},
                    "all_deaths": {self.mortes[-1]},
                    "variation_deaths_movel": {self.percent_deaths},
                    "percent_variation_death": {self.percent_all_deaths},
                    "variation_cases_movel": {self.percent_cases},
                    ""
                '''
