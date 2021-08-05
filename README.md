
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

place = 'Petrolina PE'
data_pet = cb.city(place)

```

### publishing painel data from covid on the instagram

```py
import covidbr as cb
cb.show_console(True)

cityes = ['juazeiro BA','Petrolina PE']
for city in cityes:

    data_covid = cb.data_from_city(city)
    cb.publish_painel_covid(data=data_covid,user='user_insta',password='password_insta')
```