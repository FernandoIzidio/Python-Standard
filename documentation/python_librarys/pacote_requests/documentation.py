"""
Cabeçalho - Informações adicionais a enviar para o servidor(site)

requests.get(url) - faz uma requisição get de um site/servidor, e obtem uma response

json é uma extrutura de dados usada para transferência de dados em paginas web
requests:
    get - Faz uma requisição get em algum servidor, e recebe uma response
    post(url, json) - Envia dados ao servidor
    put - Substituir dados no servidor
    patch - atualizar dados no servidor
    delete -  Remove dados do servidor

metódos de response:    
    status_code - Código de resposta da requisição
    headers -> Retorna os headers dessa response, que são informações adicionais enviadas/recebidas
    content -> Retorna conteúdo da pagina em bytes
    text -> Retorna conteudo da pagina html
    json() -> Converte conteúdo da página em json
    reason -> Motivo de sucesso/fracasso da requisição


http:// -> 80 - Serviço rodando na porta 80
https:// -> 443 - Serviço rodando na porta 443

Header:
    metódo de requisição
    status de requisição
    endereço da requisição
    codificação
    token
    content-type
    e etc

token - é uma autorização para acessar um sistema por determinado tempo
endpoints - Como usar uma api sem se preocupar com os detalhes de implementação
    
"""



import requests


url = 'http://localhost:4512/' #Requisição da home da porta 4512 no localhost

response = requests.get(url)
print(response)
if response.status_code == 200:
    print('sucess')
    dic = {1: response.text}
    temp = dic.get(int(input('[1] - Mostrar conteúdo da página\n[2] Sair\n:')))
    if temp != None:
        print(temp)


