import pytest
from django.conf import settings
from CadastroDePessoas import settings
from dotenv import load_dotenv
load_dotenv()
import django
django.setup()

DJANGO_SETTINGS_MODULE = settings.INSTALLED_APPS

from django.contrib.auth.models import User
#u = User.objects.get(username='admin_test543')

def test_create_user():
    #pytestmark = pytest.mark.django_db
    userTestCreated = User.objects.create(
        username='usuario_teste@324',
        password='senha_teste!987'
        )
    assert userTestCreated.username == 'usuario_teste@324'
    assert userTestCreated.password == 'senha_teste!987'
    assert userTestCreated.is_active
    assert not userTestCreated.is_staff
    assert not userTestCreated.is_superuser

def test_delete_user():
    userTestCreated = User.objects.get(username='usuario_teste@324')
    assert userTestCreated.delete()

def teste_create_superuser():
    #pytestmark = pytest.mark.django_db
    super_user = User.objects.create_superuser(
        username='admin_test543',
        password='senha_teste!987'
    )
    assert super_user.username== 'admin_test543'
    adminQueryPassword = User.objects.get(username='admin_test543').password#consultando no banco de dados a recem criação do super usuario
    assert super_user.password== adminQueryPassword
    assert super_user.is_active
    assert super_user.is_staff
    assert super_user.is_superuser
