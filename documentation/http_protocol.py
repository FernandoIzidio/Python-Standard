"""
Cabeçalhos são informações adicionais para serem enviadas em uma requisição ao servidor, pode conter a codificação(da requisição), a lingua, o id da sessão e etc


HyperText Transfer Protocol - Protocolo usado para transferência(enviar e receber dados) de dados na internet
Ele funciona no modo cliente/servidor:
    - Onde o cliente(navegador) faz uma requisição
    - E seu servidor(site) response com dados adequados(retorna uma response).

Metódos essenciais do Protocolo (Http) - cliente side:
    - readmethods(retornam dados):
                -get - Pesquisa na ferramenta de busca, acesso nas paginas de um site e etc, metódo utilizado para receber dados do servidor
                -head - Cabeçalho do site
                -options - Metódos suportados
    - writemethos(enviar dados/ escrita):
        post - normalmente usado em formulario/ cadastros, para enviar dados ao servidor, metódo utilizado para enviar dados para o servidor, ou dados sensiveis
        put - para substituir dados no servidor, pode ser uma troca de senha por exemplo, ou trocar um conjunto de palavras em documento html
        patch - para atualizar um titulo por exemplo
        delete - apagar alguma coisa no documento
    - endereço do recurso a ser acessado (/users/)
    - Os cabeçalhos http (Content-Type, Autorization)
    - O corpo da requisição

Metódos essenciais do Protocolo(HTTP) - Server Side:
    - Status de requisição (200 sucess, 404 - Not Found(Requisição não encontrada), 301 - Moved Permanently)
    - cabeçalhos http
    - corpo da requisição - Retorno a requisição

Criar servidor http no computador, para receber dados de requisição.


file: Protocolo de arquivo no SO, conhecido como FTP

python -m: 
    Executa módulo python como script

python -m http.server -d way port - Serve uma pagina html no localhost
    Executa o módulo python como script
    passa http.server como argumento de script
    -d informa o diretorio do site 
    port a porta em que serviço vai ser aberto/servido


Só é permitido um serviço por porta, se tiver mais de um serviço rodando na porta e eu tentar hospedar nessa porta outro serviço a hospedagem vai dar erro.
Resumindo uma porta por serviço

http:// -> 80 - Serviço rodando na porta 80
https:// -> 443 - Serviço rodando na porta 443

"""