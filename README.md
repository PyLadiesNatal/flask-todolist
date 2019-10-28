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
