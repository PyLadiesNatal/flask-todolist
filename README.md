# flask-todolist

Um exemplo de aplicação Flask feita em Python para listar tarefas.

### criar uma virtualenv chamada `env`

```
# pyenv
pyenv virtualenv 3.7.4 env
# virtualenv
virtualenv -p python3 env
```

### onde está sua `env`?

```
# pyenv
pyenv versions
```

Se você usar a `virtualenv`, basta dar um `ls` no seu terminal, e vai ver o diretório criado por ela.

### ativar o ambiente

```
# pyenv
pyenv activate env
# virtualenv
source /env/bin/activate
```

### instale as bibliotecas necessárias para o projeto

```
pip install -r requirements.txt
```

### O que será feito na aplicação

 - [ ] Menu - Nome do usuário.
 - [ ] Menu - Todas as listas.
 - [ ] Menu - Hoje.
 - [ ] Menu - Próximos 7 dias.
 - [ ] Menu - Calendário.
 - [ ] Menu - Configurações.
 - [ ] Menu - Etiquetas.
 - [ ] Criar lista de tarefas com um tema específico.
 - [ ] Adicionar tarefa.
 - [ ] Editar tarefa.
 - [ ] Excluir tarefa.
 - [ ] Marcar como feita.
 - [ ] Incluir seção.
 - [ ] Exibir, na mesma tela, as tarefas pendentes e as concluídas (opcional).
 - [ ] Compartilhar Lista com outra pessoa.
 - [ ] Ordenar da Lista.
 - [ ] Tarefas diárias (Se repetem em muitos dias).