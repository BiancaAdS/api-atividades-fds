# API Atividade Fast Design Sprint

API implementada para o TCC: 
**"Instanciação e Avaliação de modelo de agenda do Design Sprint para uso em um Hackathon"**.
Para a implementação da aplicação foi utilizado Django Framework para realizar o desenvolvimento da API responsável por realizar o cadastros das atividades para serem utilizadas na Aplicação web Fast Design Sprint.

## Instalação
Antes de iniciar, você deve realizar o clone desse repositório (ou baixar o zip com o código-fonte):

`git clone https://github.com/BiancaAdS/api-atividades-fds.git`


`cd api-atividades-fds`

Após realizar o clone do repositório, crie um ambiente virtual e instale as dependências para a execução do projeto disponíveis no arquivo requirements.txt:

Com o pip, instale o virtualenv:

*pip install virtualenv*

Ao finalizar a instalação do virtualenv, dentro do diretório fast-design-sprint-fb, basta dar o comando:

*virtualenv venv*

O nome *venv* é o nome de exemplo escolhido para o ambiente virtual, caso deseje pode ser escolhido outro nome para o ambiente.

Para realizar a ativação do ambiente virtual, execute o seguinte comando na pasta bin:

*source venv/bin/activate*

Com o ambiente virtual ativado, instale os requisitos para a execução da aplicação:

`pip install -r requirements.t`

Antes de iniciar a execução da aplicação, deve-se realizar algumas mudanças no arquivo *settings.py*.
Caminhe até o diretório fast_design_sprint e realize as seguintes edições no arquivo *setting.py*:
- Localize a seção *DEBUG* e realize a troca de False para True:

    `DEBUG = True`
- Nesse mesmo diretório, crie o arquivo *.env* e insira as informações da *DATABASES* e *SECRET_KEY*:
    ```
    NAME=NomeDatabase
    USER=UsuarioDatabase
    PASSWORD=SenhaDatabase
    HOST=HostDatabase
    PORT=PortDatabase
    SECRET_KEY=SecretKey
    ```

Caso queira gerar uma SECRET_KEY, execute o seguinte comando: `python -c "import secrets; print(secrets.token_urlsafe())"`


## Rodando localmente

Após realizar todas as instalações, se tudo estiver correto, você já pode rodar o servidor de desenvolvimento e testar a aplicação. 
O seguinte comando deve ser executado no diretório que contém o arquivo *manage.py*:

`python manage.py runserver`


Para acessar a aplicação acesse: ` http://127.0.0.1:8000/ ` 
Para acessar a documentação acesse: ` http://127.0.0.1:8000/swagger `
