from PIL import ImageFont
from PIL import ImageDraw 
from PIL import Image
from covidbr.log.logging import log
import os
import requests as rq


#### painel covidb #### 
def create_painel(data,limit_period:str=15,path_file:str='painel_covid.jpg'):
        log('creating the image')
        self = data
        size = limit_period
        if not os.path.isfile('painel_covid.png'):
            content_img = rq.get('')

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
        log('ateh aqui blz,')
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

        
        img.save(path_file)
        
        return f'''
                    "date_update": {self.date[-1]},
                    "all_confirmeds": {self.casos[-1]},
                    "all_deaths": {self.mortes[-1]},
                    "variation_deaths_movel": {self.percent_deaths},
                    "percent_variation_death": {self.percent_all_deaths},
                    "variation_cases_movel": {self.percent_cases},
                    ""
                '''
