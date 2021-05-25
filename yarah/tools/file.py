
from .puts import puts

def save_file(var,path,code='utf-8',a='wb'):

  with open(path,a) as _file:
    puts('salvando variavel...')
    _file.write(str(var))
    puts('variavel salva!')



def create_file(path:str, content:str) -> bool:
	try:
		with open(path, 'wb') as file:
			file.write(content)
		return True
	except:
		raise
		return False

def create_file_json(path:str, content:dict) -> bool:
	if(type(content == dict)): 
		raise Exception(f'content is not a dict! Is a {type(content)}')
	try:
		content = json.dumps(content)
	except:
		raise

	return create_file(path=path, content=content)




#salvando arquivos
def save_file(var,path,code='utf-8',a='w'):
  with open(path,a,encoding=code) as _file:
    puts('salvando variavel...')
    _file.write(str(var))
    puts('variavel salva!')
