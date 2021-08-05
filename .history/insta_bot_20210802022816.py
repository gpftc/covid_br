import covidbr as cb
cb.show_console(True)
#data_covid = cb.data_from_city('Recife PE')
#cb.create_painel(data=data_covid,path_file='painel_jua.jpg')
cityes = ['paulo afonso BA','casa nova BA','juazeiro BA','Petrolina PE']
for city in cityes:
    data_covid = cb.data_from_city(city)
    cb.publish_painel_covid(data=data_covid,user='gpftc_ifsertao',password='imaginando912')