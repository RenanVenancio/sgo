# Sistema de gestão de ocorrências
Gestão de ocorrências: Engenharia Civil &amp; Sistemas para Internet <br />
Sistema que automatiza e controla as etapas de solicitações de assistência técnica para edifícios já construídos, dando suporte aos usuários das unidades habitacionais bem como favorecendo a construtora que o utilizar. O utiliza de tecnologias web onde tem o foco inicial de sua aplicação.

### Documentação gravação e maiores detalhes sobre o sistema
https://drive.google.com/drive/folders/1sTZow1sOBotXqkleQQYKiKOBw-j6StNC?usp=sharing

### Instalando

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

