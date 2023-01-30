# CNAB-file-reader

Esta aplicação lê e interpreta arquivos .txt no padrão CNAB, salvando os dados das operações no banco de dados.

## Como rodar o projeto

1. Criar um ambiente virtual:

```
python -m venv venv
```

2. Ativar o ambiente virtual:

- No Linux:

```
source venv/bin/activate
```

- No Windows:

```
.\venv\Scripts\activate
```

3. Instalar as dependências do projeto:

```
pip install -r requirements.txt
```

4. Criar um arquivo .env na raiz do projeto com as credenciais do seu database e a secret key, seguindo o padrão do .env.example

5. Persistir as migrações no database:

```
python manage.py migrate
```

6. Rodar o servidor:

```
python manage.py runserver
```

## Endpoints disponíveis

### api/operations/

- GET: lista todas as operações salvas no banco de dados;
- POST: salva um conjunto de operações no banco de dados. Só permite o envio de arquivos .txt no padrão CNAB;

### api/stores/

- GET: lista todas as lojas com seus respectivos saldos (balance) e operações.
