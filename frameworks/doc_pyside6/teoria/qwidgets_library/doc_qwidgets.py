"""
C++/Qt 
Classes - PascalCase
metódos/funções/atributos/variaveis - camelCase

Widgets(window get) - São elementos interativos que compõem uma aplicação

QPushButtom('Conteúdo do botão') - Cria um botão de apertar
QLabel('Conteúdo') -  é um widget que exibe um texto ou uma imagem, é util para mostrar informações visuais ao usuário
QlineEdit - Widget para input's curtos de usuário, ou seja entradas de usuários de no máximo uma linha
QTextEdit - Widget para input's longos de usuário, ou seja entradas de dados longos de usuário.
QStatusBar - Barra usada para exibir informações sobre a aplicação
QMenuBar - Menu da aplicação




Metódos uteis de Widgets:
    show() - Mostra o botão
    setStyleSheet(Qss:str) - Defina a estilização de um botão
    self.font() -> QFont  - Permite alterar caracteristicas da fonte de um widget(elemento interativo)
    setProperty(name:str, value:str) - Define uma propriedade/atributo em um widget
    self.text() - Retorna o conteúdo do widget
    self.setText() - Define o conteúdo do widget 
    self.insertText() - Adiciona conteúdo, ao conteúdo atual do widget
"""