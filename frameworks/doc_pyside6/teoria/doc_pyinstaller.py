"""
Pyinstaller é um excelente módulo/biblioteca para compilação de código python, ele gera um executavel que elimina a
necessidade de ter o python baixado no computador, para executar um programa
Obs: Usar sempre caminhos relativos para maior facilidade
windows = ;
linux = :
--name - nome do executavel
--onefile - Gera apenas um arquivo executavel
--noconfirm - Não pede nenhuma confirmação para qualquer operação
--noconsole - Não abre o console durante a execução da aplicação
--clean - Não persiste os dados da aplicação
--add-data - Adiciona o caminho dos arquivos não script
--icon - Define o icon do executavel
--log-level=  - Define os tipos de aviso que vai receber durante a compilação
--distpath - Define onde vai ser salvo o diretório dist, usar sempre caminho relativo ao configfile
--workpath - Define onde vai ser salvo o diretório build,  usar sempre caminho relativo ao configfile
--specpath - Define o caminho do configfile

o arquivo config file(.spec) detém as configurações da aplciação, e pode ser usado para reconstruir a aplicação

Example command:
    pyinstaller --name "Calculadora" --noconfirm --add-data="calculadora/images:images"
    --icon="calculadora/images/icon.png" --noconsole --clean --log-level=WARN
    --distpath="/home/pennpc/Desktop/" --workpath="/home/pennpc/Desktop/"
    --specpath="/home/pennpc/Desktop" calculadora/main.py


"""



