"""
É util para fazer raspagem de dados, e extrair dados de paginas web de forma simples

Apenas com o codigo binário é possivel rescreever imagens e videos

    htmlparser =  BealtifulSoup(dochtml/xml, 'html.parser') - Transforma todos os elementos do doc html em objetos python

    htmlparser = BealtifulSoup(bytes, 'html.parser', from_encoding) - transforma todos os elementos de um documento html em objetos python, com um codificação em especifico

pythonw modulo - Executa módulo python em segundo plano

htmlparser -
        .tag - Retorna a tag e seu conteudo
        .text - Retorna conteudo da tag
        .string - Retorna conteudo da tag
        .name - Retorna nome da tag
        select - Seleciona todas as tags, com base em regras css
        select_one - Seleciona uma tag baseada no seletor css

"""
import requests, bs4, pathlib, os
currentdir = pathlib.Path(__file__).parent
os.chdir(currentdir.__str__())



url = "http://localhost:3001/" # Faz requisição na home do site servido na porta 3001 do local host


(currentdir  / "servidor.py").touch(exist_ok=True)
while True:
    try:
        response = requests.get(url)

        if response.status_code in range(200, 300):
            html = response.text
            htmlparsed = bs4.BeautifulSoup(html, 'html.parser')
            print(htmlparsed.title.text)
            print(htmlparsed.title.name)
            tagselected = htmlparsed.select_one("#intro > div > div > article > h2")

            print(tagselected)
            print('\n')
            print('\n')
            print(tagselected.parent)
            print('\n\n\n\n')
            print(tagselected.parent.text)

            if input('press q to quit:').lower() == 'q':
                break
    except:
        os.system(f"pythonw {(currentdir /  'servidor.py').__str__()}")
        print('Subindo o servidor')
        continue
