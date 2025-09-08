# Desafio de Projetos [SQUAD 4]

## Contribuindo

Para contribuir, é necessário instalar o gerenciador de pacotes e projetos `uv`, instruções disponíveis nesse [link](https://docs.astral.sh/uv/#installation).
Feito isso, clone o repositório, mude o seu diretório para a pasta clonada e sincronize o projeto `uv`. Da seguinte maneira:

```bash
git clone https://github.com/fabriciomj/desafio-squad4-back.git
cd desafio-squad4-back
uv sync
```

Esse comando uv vai instalar as dependências do projeto. Feito isso, está pronto. Além disso, com o `uv`, quando você for executar um comando python, adicione `uv run` antes para rodá-lo de dentro do ambiente virtual do projeto. Por exemplo:

```bash
uv run manage.py runserver
uv run python --version
uv run python -m django --version
```
