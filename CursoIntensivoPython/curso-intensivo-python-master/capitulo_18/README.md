### Passos para controlar a criação de uma aplicação web com Django
1. Isolar o projeto é muito importante antes de mais nada, então utilizando o comando 
`$ python   -m   venv   ll_env` você cria um ambiente virtual.
2. Para ativar o ambiente virtual, usa-se o comando `$ source  ll_env/bin/activate` e no 
Windows `$ ll_env\Scripts\activate`, para desativar o ambiente é só digitar `$ deactivate`, 
ele também se tornará inativo se fechar o terminal em que estiver executando.
3. Instalar o Django com o comando `$ pip install django`. O Django só estará disponível
quando o ambiente virtual estiver ativo.
    > i. Para criar um projeto em Django, sem sair do ambiente virtual, usa-se o comando:

    >- `$ django-admin.py startproject learning_log .`

    > _Esse ponto no final é muito importante, ele cria o novo projeto com uma estrutura de
    diretórios que facilitará a implantação da aplicação em um servidor._

    > ii. Após executar o comando, uma nova pasta chamada _learning_log_ é criada. Além 
    dela, também é criado um arquivo chamado _manage.py_, ele é um pequeno programa que 
    aceita comandos e os passa para a parte relevante de Django que os executa. Ele é 
    muito usado para administrar bancos de dados e executar servidores.

    > iii. Dentro do diretório _learning_log_ que foi criado, existem 4 outros arquivos.
    Os mais importantes são: _settings.py_, _urls.py_ e _wsgi.py_.

    >- `settings.py` - Controla o modo como Django interage com o seu sistema e administra
    o seu projeto. 
    >- `urls.py` - Informa a Django quais páginas devem ser criadas em resposta a requisições
    do navegador.
    >- `wsgi.py` - Ajuda Django a servir os arquivos que ele criar. O nome do arquivo é um 
    acrônimo para _web server gateway interface_ (interface de gateway do servidor web).

### Criando o banco de dados
Como o Django armazena a maior parte das informações relacionadas a um projeto em um banco
de dados, precisamos criar um para que o framework possa trabalhar com ele. O comando para 
criar um é `$ python manage.py migrate`.
>- É criado um arquivo chamado _db.sqlite3_, é um banco de dados que executa com base em um
único arquivo; é ideal para escrever aplicações simples, pois você não precisará prestar muita
atenção no gerenciamento do banco de dados.

### Visualizando o projeto e criando uma aplicação
- Para rodar um servidor local do projeto e ver se o Django está funcionando corretamente,
usa-se o comando `$ python manage.py runserver`. O URL _http://127.0.0.1:8000/_ informa que
o projeto está ouvindo requisições na porta 8000 de seu computador – chamada de localhost. 
O termo localhost se refere a um servidor que processa requisições somente em seu sistema; 
ele não permite que outras pessoas vejam as páginas que você está desenvolvendo. Para interromper
o servidor é só digitar `CTRL + C`.

- Um projeto Django é organizado na forma de um grupo de aplicações(apps) individuais que 
operam em conjunto para fazer o projeto funcionar como um todo. Para criar uma app que irá
fazer a maior parte do trabalho do projeto usa-se o comando **`$ python manage.py startapp
learning_logs`**. Esse comando diz para o Django criar a infraestrutura necessária à construção
de uma aplicação.
    > i. Após isso, uma pasta chamada _learning_logs_ será criada com alguns arquivos. Os mais
    importantes são: _models.py_, _admin.py_ e _views.py_.

    >- `models.py` - Defini os dados que queremos administrar em nossa aplicação.
    >- `admin.py` - Registra as classes de `models.py` da aplicação no site de administração.
    >- `views.py` - Armazena as funções da aplicação, cada função obtém e processa os dados 
    necessários de um determinado _URL_ e também chama um template para esse _URL_.

### Informações Extras
- Sempre que quisermos modificar os dados administrados por _Learning Log_, executaremos
estes três passos: modificaremos `models.py`, chamaremos _makemigrations_ em _learning_logs_
e diremos a Django para executar um _migrate_ no projeto.
- Geralmente a criação de páginas web com Django é constituída de três etapas: definir os _URLs_,
escrever as _views_ e criar os _templates_.
- Para ativar o shell de Django em uma ambiente virtual usa-se o comando `$ python manage.py shell`,
para interromper ele é só digitar `CTRL + Z` e depois `ENTER` no Windows.
