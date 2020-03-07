# Curriculo-Gerenciavel-Django
Currículo gerenciável que renderiza no template as informações adicionadas no bd pelo usuário

# Como iniciar a applicação
1. Criar uma máquina virtual:
  $ python3.7 -m venv venv
   
2. Ativar a máquina virtual:
  $ source venv/bin/activate (no linux)
  
  $ cd venv/Scripts
  $ activate (no windows)
  
3. Instalar todas as bibliotecas necessárias para a aplicação:
  $ pip3 install -r requirements.txt
  
4. Rodar a aplicação:
  $ python manage.py runserver

# Como criar seu currículo com esta aplicação
1. apagar o arquivo db.sqlite3

2. atualizar o banco de dados:
    $ python manage.py migrate

3. criar um super-usuário para administrar o bd:
    $ python manage.py createsuperuser
Inserir nome de usuário e senha

4. rodar a aplicação
    $ python manage.py runserver
O currículo aparecerá vazio pois nenhuma informação foi adicionada ao bd até então

5. Preencher o bd acessando o endereço de administrador:
     http://127.0.0.1:8000/admin
entrar com usuário e senha criados no passo 3

6. Preencher o bd com suas informações

OBS: As tabelas 'Objetivo' e 'Sobre' terão apenas uma instância, pois oo currículo pertente a uma só pessoa
