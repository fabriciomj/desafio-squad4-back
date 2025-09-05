# Deploy no PythonAnywhere

Esse documento é uma adaptação do [tutorial](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject) 
para o projeto do desafio.

## Primeiros passos

Depois de criada a conta no site, acesse a tela de Dashboard e
abra um novo console Bash, executando os seguintes comandos:
```bash
pip install --upgrade "uv==0.8.15"
git clone https://github.com/fabriciomj/desafio-squad4-back.git
cd desafio-squad4-back
uv sync
```
Isso ira atualizar o uv para a versão utilizada no projeto, clonar o repositório e sincronizar o venv do repositório local.

## Configurando o Web app

### Virtualenv

Certifique-se de inserir `/home/fabriciomj/desafio-squad4-back/.venv` na seção `Virtualenv` da tela de configuração do Web app.
Além disso, a versão Python a ser utilizada será a versão `3.13`.

### Caminho de Código

Insira o caminho do repositório clonado: `/home/fabriciomj/desafio-squad4-back`.

### Editando o arquivo WSGI

Basta copiar o arquivo presente na pasta `deploy` do projeto:
```bash
cd desafio-squad4-back/deploy/
cp ./fabriciomj_pythonanywhere_com_wsgi.py /var/www/
```

## Configurando o Banco de Dados

Para configurar o banco de dados, é preciso utilizar o script `manage.py` com o argumento `migrate`, a partir do
Django do virtualenv, utilizando o prefixo `uv run` para isso.
```bash
cd desafio-squad4-back/
uv run manage.py migrate
```