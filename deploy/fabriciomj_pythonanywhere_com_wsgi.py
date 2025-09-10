import os
import sys

from django.core.wsgi import get_wsgi_application

# Caminho no qual o repositório foi clonado.
path = "/home/fabriciomj/desafio-squad4-back"
if path not in sys.path:
    sys.path.append(path)

# Nome do projeto escolhido durante o comando "django-admin startproject", nesse
# caso "squad4".
os.environ["DJANGO_SETTINGS_MODULE"] = "squad4.settings"

application = get_wsgi_application()
