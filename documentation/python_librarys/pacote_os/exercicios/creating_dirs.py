from os import walk, path, system, mkdir, listdir


way = path.join(path.abspath('.'), 'pacote_os','exemplo')
print(way)

if not path.exists(way):
    mkdir(way)


for count in range(10):
    subdirectory = path.join(way, f'Pasta_{count+1}')

    if not path.exists(subdirectory):
        mkdir(subdirectory)
    
    for count in range(5):
        waytemp = path.join(subdirectory, f"text{count+1}.txt")
        system(f'echo FLAMENGO É PIADA!!!! >> {waytemp}')    

walk('.')
