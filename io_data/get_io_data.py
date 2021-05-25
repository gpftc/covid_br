from .browser import browser


def get_io_data(city,state,name,password):
   
    print('abrindo site...')
    url = (f'https://brasil.io/dataset/covid19/caso_full/?state={state}&city={city}&format=csv')
    res = br.get(url)

    #salva os status da pagina
    res.raise_for_status()
    if ("entrar" in str(res.content)):
        #print(res.content)
        print('Atenção: login requerido!')
        
        br.open(url)
        print(f'enviando dados de login [nome:{name}, senha: {password}]...')
        
        br.select_form()
        br['username'] = name
        br['password'] = password
        br.launch_browser()
        print('Login enviado!')
        
        res = br.submit_selected()
        
        if('tente novamente' in str(res.content)):
            print("Login incorreto!")
            return False 
            
        else:
            print('Login aceito!')
            filename = f'{city}.csv'
            print(f'tentando baixar {filename}...')
            
            res = br.get(url)
            res.raise_for_status()
            
            with open(filename,'wb') as file:
                file.write(res.content)
            print('verifica ai se foi')
            
            return filename
