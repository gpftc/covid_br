#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################
## author: Reinan Br. ##
## date: 25/06/2021   ##
## project: API_covid ##
########################

from covidbr.log import logging
from covidbr.api_io.api_io_request import get_data_covid,login_io
from covidbr.get_data import data_from_city
from covidbr.plot_data.plotting import plot_media_cases
from covidbr.plot_data.plotting import plot_media_deaths
from covidbr.plot_data.painel import create_painel



all = [data_from_city,
       login_io,logging,
       get_data_covid,
       plot_media_cases,
       plot_media_deaths,
       create_painel
]