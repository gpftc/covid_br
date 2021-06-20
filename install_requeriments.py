import os


def date():
    from datetime import datetime as dt
    dt = dt.now()
    return dt.strftime('%d/%m/%Y %H:%M:%S')

def puts(*args,sep=' ',path_file=None):
    input = ''
    for i in args:
        input += i+sep
  #  cpu = f'[CPU: {ram()[2]}%_{ram()[3]}ms]\n' if(__cpu_show__) else ''
    text = (f'[{date()}]: {input}')
    print(text)
    if path_file:
        path = open(path_file,'a',encoding='utf-8')
        with path as file_p:
            file_p.write(text+'\n')
            # TODO: write code...

class bcolors:
    CGREEN  = '\33[32m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def terminal_python3(comand:str):
    puts(f'py>> {comand}')
    return os.popen(f'python3 -c "{comand}"')
########################### install_pip def ######################
def install_pip(lib_name:str):
    try:
        cmd = os.system
        puts(f'{bcolors.OKCYAN}installing {lib_name}...{bcolors.ENDC}')
        try:
            cmd('pip install pandas')
        except:
            puts(f'{bcolors.FAIL}error {lib_name} not installing!{bcolors.ENDC}')
            raise
        puts(f'{bcolors.WARNING}verifyng import {lib_name}...{bcolors.ENDC}')
        terminal_python_test = terminal_python3(f'import {lib_name};print({lib_name})')
        if('module' in terminal_python_test.read()):
            puts(f'{bcolors.CGREEN}import {lib_name} ok!{bcolors.ENDC}')
        else:
            puts(f'{bcolors.FAIL}{lib_name} not found or working! {bcolors.ENDC}')
            #raise ModuleNotFoundError
            exit()
    except KeyboardInterrupt:
        puts('user requeriment interruption')
        exit()



def install_pip_list(list_lib_names:list):
    try:
        size_list = len(list_lib_names)
        i = 0
        for lib in list_lib_names:
            i += 1
            print(20*'=+=')
            puts(f'[{i}/{size_list}] => {lib}')
            install_pip(lib)
    except KeyboardInterrupt:
        puts('user requeriment interruption')
        exit()


list_packages = ['pandas','matplotlib','mechanicalsoup','psutil','geopy']
install_pip_list(list_packages)