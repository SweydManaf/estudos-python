### Resumo do Capítulo
Neste capítulo foi ensinado a usar formulários para permitir que os usuários
adicionem novos assuntos e entradas, além de editar entradas existentes. Então
foi visto também como implementar contas de usuários. Permitir que usuários 
existentes fizessem _login_ e _logout_ e a usar o [_UserCreationForm_](https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.forms.UserCreationForm)
default de **Django** para que as pessoas pudessem criar novas contas. Depois de 
desenvolver um sistema simples de autenticação e de cadastro de usuários, 
restringir o acesso a determinadas páginas aos usuários logados usando o decorador [_@login_required_](https://docs.djangoproject.com/en/2.2/topics/auth/default/#the-login-required-decorator).
Então foi atribuído dados a usuários específicos por meio de um relacionamento de [_ForeignKey_](https://docs.djangoproject.com/en/2.2/ref/models/fields/#foreignkey).
Também foi aprendido a migrar o banco de dados quando a migração exige que você 
especifique alguns dados _default_. Por fim, foi visto como garantir que um usuário 
possa ver apenas os dados que lhe pertencem, modificando as funções de _view_. Recuperar
os dados apropriados usando o método [_filter()_](https://docs.djangoproject.com/en/2.2/topics/db/queries/#retrieving-specific-objects-with-filters)
e foi aprendido a comparar o dono do dado solicitado com o usuário logado no momento: 

```
from django.http import Http404

def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404
```

> _Nem sempre será óbvio de imediato quais dados devem ser disponibilizados e quais devem ser 
protegidos, mas essa habilidade será adquirida com a prática. As decisões que foram tomadas neste
capítulo para proteger os dados dos usuários mostram por que trabalhar com outras pessoas
é uma boa ideia quando um projeto é desenvolvido: ter alguém para observar o seu projeto faz com 
que seja mais provável identificar áreas vulneráveis._

### Informações Extras
- Na página 503 fala sobre a importância de migrar um banco de dados ao mesmo tempo em que a integridadde
dos dados dos usuário é mantida. Mas podemos simplesmente reiniciar o banco de dados em vez de fazer uma migração,
isso perderia todos os dados existentes. Mas isso se encaixa no caso de se caso você queira recomeçar com um banco
de dados limpo, simplesmente fazer uma formatação no banco de dados excluíndo absolutamente tudo sobre todos os dados, 
execute o comando `python manage.py flush` para recriar o banco de dados. Você deverá também criar um novo **superusuário**.
