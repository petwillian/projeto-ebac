#Criar uma conta no GitHub.
#Criar um personal access token.
#Configurar a conexão entre o git local com o git remoto (GitHub):

import os

username = "<seu-usuario-git>" # insira o seu nome de usuário do git
os.environ["GITHUB_USER"] = username

!git config --global user.name "${GITHUB_USER}"

import os
from getpass import getpass

usermail = getpass()
os.environ["GITHUB_MAIL"] = usermail

!git config --global user.email "${GITHUB_MAIL}"


import os
from getpass import getpass

usertoken = getpass()
os.environ["GITHUB_TOKEN"] = usertoken

#Projeto

#Criar o projeto remoto.
#Fazer o download do projeto remoto na máquina local

!git clone https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/petwillian/projeto-ebac.git

%cd /content/projeto-ebac/

#Criar um arquivo e salvar as aterações no repositório local.

!touch projeto-git.py
!git status

!git add projeto-git.py
!git status

!git commit -m "arquivo projeto-git.py criado"
!git status

#Enviar as alterações para o repositório remoto

!git push origin main
!git status

