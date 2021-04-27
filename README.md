# Sistema de gestão de ocorrências

O sistema realiza o gerenciamento e acompanhamento de ocorrências em edifícios já construídos.
Sistema 100% Web, possui uma API para integração com outros sistemas.

# Deploy
<a href="http://sgoengenharia.herokuapp.com/">http://sgoengenharia.herokuapp.com/</a>
<p>Usuário: <b>root</b></p>
<p>Senha: <b>venancio123</b></p>


### Executando projeto na máquina local

Primeiro passo será a criação de uma máquina virtual (os comandos são para serem aplicados em Sistema Operacional Windows, há variações para Linux/OSX)

```
python -m venv nome-da-maquina-vitual
```

Vamos executar a maquina virtual

```
nome-da-maquina-virtual\Scripts\activate
```

Acesse a pasta do projeto e instale as dependências com o comando

```
pip install -r requirements-dev.txt
```

### Configurando Banco de dados

Na pasta do projeto vamos fazer a migração

```
python manage.py makemigrations

```

Agora vamos gerar o banco

```
python manage.py migrate

```

### Executando o projeto

```
python manage.py runserver
```

Acesse o site pelo endereço
	
<a href="http://localhost:8000">http://localhost:8000</a>


### API do sistema
<p>O sistema possui uma api para integração com o aplicativo
Para acessar a documentação da API</p>



<a href="http://localhost:8000/api/docs/">http://127.0.0.1:8000/api/docs/</a>

