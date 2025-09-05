import os
import sys

# Caminho no qual o repositório foi clonado.
path = '/home/fabriciomj/desafio-squad4-back'
if path not in sys.path:
    sys.path.append(path)

# Nome do projeto escolhido durante o comando "django-admin startproject", nesse 
# caso "squad4".
os.environ['DJANGO_SETTINGS_MODULE'] = 'squad4.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()