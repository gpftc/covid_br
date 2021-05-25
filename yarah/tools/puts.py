from ..system import date, cpu_info, ram



def puts(*args,sep=' ',path_file=None):
  input = ''
  for i in args:
    input += i+sep
  cpu = f'[CPU: {ram()[2]}%_{ram()[3]}ms]\n' if(__cpu_show__) else ''
  text = (f'{cpu}[{date()}]: {input}')
  print(text)
  if path_file:
    path = open(path_file,'a',encoding='utf-8')
    with path as file_p:
      file_p.write(text+'\n')
      # TODO: write code...
 
