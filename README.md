## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

1.  **Clone o repositório:**
    ```bash
    git clone <https://github.com/jaofe/mv-backend>
    cd mv-backend
    ```

2.  **Crie e ative um ambiente virtual:**
    - No Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto, copiando o conteúdo de `.env.example` (se existir) ou usando o exemplo abaixo. Substitua os valores conforme necessário.

    ```env
    # Configurações do Banco de Dados
    DB_DRIVER="postgresql"
    DB_USER="postgres"
    DB_PASSWORD="sua_senha"
    DB_HOST="localhost"
    DB_PORT="5432"
    DB_NAME="mv_db"

    # Chave secreta para JWT
    SECRET_KEY="sua-chave-secreta"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES="30"

    # Configurações de Email/SMTP
    MAIL_USERNAME="seu-email@gmail.com"
    MAIL_PASSWORD="sua-senha-de-app"
    MAIL_FROM="seu-email@gmail.com"
    MAIL_PORT="587"
    MAIL_SERVER="smtp.gmail.com"
    MAIL_STARTTLS="True"
    MAIL_SSL_TLS="False"

    # Configurações do Cloudinary (opcional)
    CLOUDINARY_API_KEY=""
    CLOUDINARY_API_SECRET=""
    ```

## Configuração do Banco de Dados

Este projeto usa o Alembic para gerenciar as migrações do banco de dados.

1.  Certifique-se de que seu servidor de banco de dados (ex: PostgreSQL) está em execução.

2.  Crie o banco de dados especificado na variável `DB_NAME` no seu arquivo `.env`.

3.  Aplique as migrações para criar as tabelas:
    ```bash
    alembic upgrade head
    ```
    Isso aplicará todas as migrações pendentes que estão na pasta `alembic/versions`.

## Executando a Aplicação

Para iniciar o servidor de desenvolvimento, execute o comando abaixo na raiz do projeto:

```bash
uvicorn app.main:app --reload
```

-   `app.main:app`: informa ao uvicorn onde encontrar a instância do FastAPI.
-   `--reload`: faz com que o servidor reinicie automaticamente após alterações no código.

O servidor estará disponível em `http://127.0.0.1:8000`.

## Uso

Após iniciar a aplicação, você pode acessar a documentação interativa da API (gerada pelo Swagger UI) no seguinte endereço:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Lá você encontrará todos os endpoints disponíveis, seus parâmetros e poderá testá-los diretamente do navegador.
