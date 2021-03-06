
<h1 align='center'>CovidBr</h1>
<p align='center'>
<img height='200px' width='200px' src='https://raw.githubusercontent.com/gpftc/covid_br/main/covidbr/img/covidbr_logo.png'>
<br/>
<a href="https://github.com/perseu912"><img title="Autor" src="https://img.shields.io/badge/Autor-reinan_br-blue.svg?style=for-the-badge&logo=github"></a>
<br/>
<a href='http://dgp.cnpq.br/dgp/espelhogrupo/0180330616769073'><img src='https://shields.io/badge/cnpq-grupo_de_fisica_computacional_ifsertao--pe-blueviolet?logo=appveyor&style=for-the-badge'></a>

<p align='center'>
<!-- github dados -->
<a href='https://python.org'><img src='https://img.shields.io/github/pipenv/locked/python-version/gpftc/covid_br'></a>
<a href='#'><img src='https://img.shields.io/github/languages/code-size/gpftc/covid_br'></a>
<a href='#'><img src='https://img.shields.io/github/commit-activity/m/gpftc/covid_br'></a>
<a href='#'><img src='https://img.shields.io/github/last-commit/gpftc/covid_br'></a>
<br/>
<!-- sites de pacotes -->
<a href='https://pypi.org/project/covidbr/'><img src='https://img.shields.io/pypi/v/covidbr'></a>
<a href='#'><img src='https://img.shields.io/pypi/wheel/covidbr'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/covidbr"></a>
<a href='#'><img src='https://img.shields.io/pypi/implementation/covidbr'></a>
<br/>
<!-- outros premios e analises -->
<a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/gpftc/covid_br?logo=codefactor">
</a>
<!-- redes sociais -->
<br/>
<a href='https://instagram.com/gpftc_ifsfertao/'><img src='https://shields.io/badge/insta-gpftc_ifsertao-violet?logo=instagram&style=flat'></a>
</p>
</p>
<p align='center'> <b>Library for data mining about covid-19 in brazilian cities 📈📊📚</b></p>
<hr/>

## Installation

```bash
$ pip install covidbr -U
```

## Examples

### Get data from cities

```py
import covidbr as cb
cb.show_console(True)

place = 'Juazeiro BA'
data_pet = cb.city(place)

```

### getting the light data and working with it

```py
dataset = data_city.dados
dados
```

```sh
             casos  mortos  mortes_diarias  casos_diarios  population
23/mar/2020      1       0               0              1      218162
24/mar/2020      2       0               0              1      218162
25/mar/2020      2       0               0              0      218162
26/mar/2020      2       0               0              0      218162
27/mar/2020      2       0               0              0      218162
...            ...     ...             ...            ...         ...
26/dez/2021  18752     417               0              0      218162
27/dez/2021  18752     417               0              0      218162
28/dez/2021  18752     417               0              0      218162
29/dez/2021  18752     417               0              0      218162
30/dez/2021  18752     417               0              0      218162

[648 rows x 5 columns]
```
getting the data of death's:
```py
mortos = dataset['mortos']
mortos
```

```sh
23/mar/2020      0
24/mar/2020      0
25/mar/2020      0
26/mar/2020      0
27/mar/2020      0
              ... 
26/dez/2021    417
27/dez/2021    417
28/dez/2021    417
29/dez/2021    417
30/dez/2021    417
Name: mortos, Length: 648, dtype: int64
```
getting the data of case's:
```py
casos = dataset['casos']
```

```sh
23/mar/2020        1
24/mar/2020        2
25/mar/2020        2
26/mar/2020        2
27/mar/2020        2
               ...  
26/dez/2021    18752
27/dez/2021    18752
28/dez/2021    18752
29/dez/2021    18752
30/dez/2021    18752
Name: casos, Length: 648, dtype: int64
```
getting the mortality percent:
```py
perc_m = (mortos/casos)*100
perc_m
```

```sh
23/mar/2020    0.000000
24/mar/2020    0.000000
25/mar/2020    0.000000
26/mar/2020    0.000000
27/mar/2020    0.000000
                 ...   
26/dez/2021    2.223763
27/dez/2021    2.223763
28/dez/2021    2.223763
29/dez/2021    2.223763
30/dez/2021    2.223763
Length: 648, dtype: float64
```