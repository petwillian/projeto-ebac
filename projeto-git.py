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