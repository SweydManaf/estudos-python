### Estilização do Projeto
Para a estilização, será usado a biblioteca [_Bootstrap_](https://getbootstrap.com.br/) 
(versão totalmente em PT-BR), ela possui uma coleção de ferramentas para estilização de
aplicações web para que elas tenham uma aparência profissional em todos os dispositivos
modernos, de um grande monitor de tela plana até um _smartphone_. Para isso, será usado
a aplicação [`django-bootstrap3`](https://django-bootstrap3.readthedocs.io/en/latest/).

##### O que é a aplicação `django-bootstrap3`?
É uma aplicação de _Django_ utilizada para integrar o _Bootstrap_ no projeto em questão.
Essa aplicação faz download dos arquivos necessários do _Bootstrap_, coloca em um lugar 
apropriado em seu projeto e deixa a diretivas de estilização disponíveis nos templates 
de seu projeto.

* Para instalar é bem simples, com o ambiente virtual de seu projeto ativado execute o
comando:
    
    `$ pip install django-booststrap3`

* Em seguida, adicione o código a seguir em _INSTALLED_APPS_ no arquivo `settings.py`:
    
    ```
    INSTALLED_APPS = [
        --trecho omitido--
        # Aplicações de terceiros.
        'bootstrap3',
    ]   
    ```

* Por fim, é necessário que `django-bootstrap3` inclua a _jQuery_, que é uma biblioteca
JavasScript que possibilita o uso de alguns dos elementos interativos oferecidos pelos 
templates do _Bootstrap_. Para isso, o código a seguir deve ser adicionado em `settings.py`:
    
    ```
    # Configurações para django-boostrap3.
    BOOTSTRAP3 = {
        'include_jquery': True,
    }
    ```

##### O que é o _Bootstrap_?
O _Bootstrap_ é basicamente uma grande coleção de ferramentas de estilização, ele tem também
diversos templates que podem ser aplicados no projeto para criar um estilo de modo geral. Para
ver os templates oferecidos pelo _Bootstrap_ é só ir nesse [link](https://getbootstrap.com.br/docs/4.1/examples/#content).

* O template que será usado nesse projeto será esse [_aqui_](https://getbootstrap.com.br/docs/4.1/examples/navbar-static/),
é um template simples que oferece uma barra de navegação superior simples, um cabeçalho de página
e um contêiner para o conteúdo da página.
    
    * [Aqui](https://getbootstrap.com.br/docs/4.1/components/navbar/) está a documentação necessária
     para saber mais sobre os templates de navegação do _Bootstrap_.
    
    * Será usado outro elemento do _Bootstrap_ chamado [_jumbotron_](https://getbootstrap.com.br/docs/4.1/components/jumbotron/),
    uma caixa grande que se destacará do restante da página inicial e pode conter o que você quiser.

### Implantação do Projeto no Heroku
A implantação de _Learning Log_ será feita com o [_Heroku_](https://www.heroku.com/), um
site que permite carregar o seu projeto em um de seus servidores, deixando-o disponível a
qualquer pessoa com uma conexão de internet.

- Passo a passo de como implantar o projeto no _Heroku_ no **_Windows_**:

    * Crie uma conta no [_Heroku_](https://heroku.com/), é de graça e permite testar de forma completa
    o projeto em uma implantação ativa. 
    
    * Para implantar e administrar um projeto nos servidores do _Heroku_, será preciso das ferramentas
     disponíveis no [_Heroku Toolbelt_](https://toolbelt.heroku.com/), entre no site e instale a versão
     mais recente.
     
    * Será necessário também instalar alguns pacotes que ajudam a servir projetos Django em um servidor
    ativo, em um ambiente virtual ativo execute os comandos a seguir:
    
        ```
        $ pip install dj-database-url
        $ pip install dj-static
        $ pip install static3
        $ pip install gunicorn    
        ```
        
        Execute os comandos um de cada vez.
    
        * O pacote `dj-database-url` ajuda o Django a se comunicar com o banco de dados usado pelo _Heroku_.
        * Os pacotes `dj-static` e `static3` ajudam o Django a administrar arquivos estáticos corretamente.
        * O `gunicorn` é um servidor capaz de servir aplicações em um ambiente ativo.
        
        Arquivos estáticos contêm regras de estilo e arquivos JavaScript.
        > Alguns dos pacotes necessários talvez não sejam instalados, portanto não se preocupe se vir uma 
        mensagem de erro quando tentar instalar alguns deles. O que importa é conseguir que o _Heroku_ instale
        os pacotes na implantação ativa.
     
    * O _Heroku_ precisa saber de quais pacotes o projeto depende, então use o comando `pip  freeze  >  
    requirements.txt` para gerar um arquivo que lista cada um. Ele diz para o pip escrever os nomes de
    todos os pacotes instalados no momento para o projeto no arquivo `requirements.txt`.
        
        > Será preciso adicionar `psycopg2` também nessa lista, ele ajuda o _Heroku_ a administrar o banco
        de dados ativo, à lista de pacotes. É só adicionar a linha `psycopg2>=2.6.1` na lista.
    
    * Se uma versão de Python não for especificada, o _Heroku_ usará sua própria versão default, então para
    impedir que isso aconteça, especificaremos a versão que estamos utilizando no projeto. Para isso crie um
    arquivo chamado **`runtime.txt`** no mesmo diretório de `manage.py`, dentro desse arquivo coloque a linha:
        
        ```
        python-3.7.2
        ```
        
        Coloque a versão de Python que está utilizando no projeto.
        
        > Se  você  obtiver  um  erro  informando  que  o  runtime  de  Python solicitado não está disponível,
        vá nesse [link](https://devcenter.heroku.com/) e clique em Python; em seguida, procure um link para
        "Specifying a Python Runtime". Dê uma olhada no artigo para encontrar os **runtimes** disponíveis e 
        utilize um que seja mais próximo à sua versão de Python.
    
    * Será necessário acrescentar uma seção no final de `settings.py` a fim de definir algumas configurações
    específicas para o ambiente do _Heroku_:
        
        ```
        --trecho omitido--
        # Configurações para o Heroku.
        cwd = os.getcwd()
        if cwd == '/app' or cwd[:4] == '/tmp':
            import dj_database_url
        
        DATABASES = {
            'default': dj_database_url.confi(defaul='postgres://localhost'),
        }
        
        # Honra o cabeçalho 'X-Forwarded-Proto' para request.is_secure().
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
        
        # Cabeçalhos para permitir todos os hosts.
        ALLOWED_HOSTS = ['*']
        
        # Configurações de recursos estáticos.
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        STATIC_ROOT = 'staticfiles'
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
        )
        ```
    
    * Um _Procfile_ diz ao Heroku quais processos devem ser iniciados para servir o projeto de forma apropriada. 
    É um arquivo de uma só linha que você deve salvar como **Procfile**, com um P maiúsculo e sem extensão, no 
    mesmo diretório em que está `manage.py`. Eis a linha em _Procfile_:
    
        ```
        web: gunicorn learning_log.wsgi --log-file -
        ```
    
        > Essa linha diz ao Heroku para usar o `gunicorn` como servidor e utilizar as configurações em 
        `learning_log/wsgi.py` para iniciar a aplicação. A flag log-file diz ao Heroku quais são os tipos
         de eventos que devem ser registrados no log.
    
    * Também é necessário modificar o arquivo `wsgi.py` para o Heroku:
        
        ```
        import os
        from django.core.wsgi import get_wsgi_application
        from dj_static import Cling
        
        
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
        application = Cling(get_wsgi_application())
        ```
    
    * Criar um diretório para arquivos estáticos. Crie uma pasta chamada _static_ com o path
    _learning_log/learning_log/static/_. Dentro dessa pasta crie um arquivo chamado `placeholder.txt`.
        
        ```
        Este arquivo garante que learning_log/static/ será adicionado ao projeto.
        O Django reunirá os arquivos estáticos e os colocará em learning_log/static/.
        ```
        
        > Não tem nada de especial nesse texto, ele só lembra porque foi incluído esse arquivo no 
        projeto.
     
    * Adicionar o Git no projeto para que seja mais fácil monitorar o processo de versionamento do mesmo.
    Como provavelmente o Git já vai estar instalado após a instalação do Heroku Toolbelt. Mas basicamente:
        
        * Use `$ git --version` para verificar se o Git está instalado.
        * Depois configure o git com os seguintes comandos:
            
            ```
            $ git config --global user.name "willy"
            $ git config --global user.email "william@example.com" 
            ```
    
    * Não é necessário que o Git monitore todos os arquivos do projeto, portanto diremos a ele para ignorar alguns.
    Crie um arquivo chamado `.gitignore` na pasta que contém `manage.py`. Ele deve ter o seguinte conteúdo:
        
        ```
        ll_env/
        __pycache__/
        *.sqlite3
        ```
        
        * `ll_env` - Ele é ignorado pois pode ser recriado automaticamente a qualquer momento.
        * `__pycache__/` - Contém arquivos _.pyc_, criados de modo automático quando Django executa os arquivos
        _.py_.
        * `*.sqlite3` - As alterações no banco de dados local não será monitorado, é um hábito ruim misturar o
        banco de dados local com o remoto, se algum dia for usar o SQLite em um servidor, poderá acidentalmente
        sobrescrever o banco de dados ativo com o banco de dados local de testes quando enviar o projeto para o
        servidor.
    
    * Agora é fazer o commit do estado inicial do projeto usando `$ git init`, depois `$ git add .` e por fim adicionar
    uma mensagem de commit assim: `$ git commit -m "Uma mensagem de commit."` (apenas uma mensagem de exemplo,
    mas você pode colocar qualquer uma).
    
Depois de todos esses passos, muito importantes diga-se de passagem, agora sim o projeto será **enviado para
o Heroku**, para isso os seguintes devem ser executados em um terminal:

```
$ heroku login
$ heroku create
$ git push heroku master
```
    
* `$ heroku login` - É usado para iniciar sessão no Heroku com a conta criada no site deles.
* `$ heroku create` - Cria um projeto vazio.
* `$ git push heroku master` - Diz ao Git para enviar o branch master do projeto para o repositório 
que o Heroku acabou de criar.

> Para conferir se o processo do servidor iniciou corretamente, utilize o comando `heroku ps`.

Ao executar esses comandos o projeto será instalado, mas não totalmente configurado. Se você acessar o
site que eles forneceram ao executar o comando `$ heroku create` ou executar o comando `$ heroku open`
em uma sessão de terminal, deverá ver o site já ON, mas não será possível usar a aplicação, pois o banco
de dados não foi configurado ainda.

### Configurando o banco de dados no Heroku
Para configurar o banco de dados ativo, é preciso executar `migrate` uma vez e aplicar todas as migrações
que foram geradas durante o desenvolvimento. Para executar um comando de Django e Python em um projeto no
Heroku, é só usar o comando `heroku run`, sendo assim esse é o comando para esse caso:

```
$ heroku run python manage.py migrate
```

> Será enviada uma "cópia" do banco de dados usado no desenvolvimento local, isso é bom, porque normalmente
o banco de dados local é usado para testes.

### Aperfeiçoando a implantação no Heroku
Será criado um superusuário igual foi feito localmente, e também o projeto ficará mais seguro alterando a
configuração `DEBUG` para _False_, para que os usuários não vejam nenhuma informação extra nas mensagens de
erro.

###### Criando um superusuário
Para criar um superusuário no servidor podemos usar o comando `$ heroku run python manage.py createsuperuser`
ou rodar um Bash Linux para isso com o comando `$ heroku run bash`, após isso é só usar os comandos normalmente
como se estivesse em um servidor local, mas lembre-se que você estará nas pastas do servidor. Use `python manage.py
createsuperuser` e siga o passo a passo. Após isso, é só entrar no site usando o link do endereço do site ativo
e colocar _/admin_ no final. Por exemplo _https://shrouded-refuge-94932.herokuapp.com/admin_.

###### Criando um URL amigável ao usuário no Heroku
A aplicação  pode  ser  renomeada  com  um  único  comando: `$ heroku apps:rename learning-log`, use o nome que
lhe for mais agradável.

###### Garantindo a segurança do projeto ativo
Para garantir a segurança do projeto ativo, uma coisa deve ser feita em `settings.py`:

```
--trecho omitido--
# Permite que apenas o Heroku seja o host do projeto.
ALLOWED_HOSTS =['learning-log-simple.herokuapp.com']

DEBUG = False
```

### Desenvolvimento contínuo
**Ao desenvolver seus próprios projetos para implantá-los, há um processo razoavelmente consistente para 
atualizar projetos. Inicialmente, você fará qualquer alteração necessária em seu _projeto local_.**

* Se suas alterações resultarem em algum _arquivo novo_, acrescente esses arquivos no repositório do Git 
usando o comando `git add .`. Qualquer mudança que exija uma migração de banco de dados exigirá esse comando, 
pois cada migração gera um novo arquivo de migração.

* Em seguida faça commit das alterações em seu repositório usando `git commit -am "Mensagem de commit."`. Depois 
disso, envie suas alterações para o _Heroku_ usando o comando `git push heroku master`. 

* Se você migrou seu banco de dados localmente, será necessário migrar o banco de dados ativo também. Você pode 
usar o comando `heroku run python manage.py migrate` uma única vez ou abrir uma sessão remota de terminal com 
`heroku run bash` e executar o comando `python manage.py migrate`. 

* Então acesse o seu projeto ativo e garanta que as alterações que você espera ver tenham tido efeito.
