import re
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR_NAME = 'backend'
FRONTEND_DIR_NAME = 'frontend'
NGINX_DIR_NAME = 'nginx'
DEPLOY_INFO_FILE_NAME = 'tests.yml'
CATSHARE_DOMAIN_KEY = 'catshare_domain'
TASKI_DOMAIN_KEY = 'taski_domain'
DOCKERFILE_NAME = 'Dockerfile'
DOCKERHUB_USERNAME_KEY = 'dockerhub_username'
WORKFLOW_FILE = 'catshare_workflow.yml'

for dir_name in (BACKEND_DIR_NAME, FRONTEND_DIR_NAME, NGINX_DIR_NAME):
    path_to_dir = BASE_DIR / dir_name
    if not path_to_dir.is_dir():
        msg = (
            f'В директории `{BASE_DIR}` не найдена папка проекта '
            f'`{dir_name}/`. Убедитесь, что у вас верная структура проекта.'
        )
        raise AssertionError(msg)


@pytest.fixture(scope='session')
def backend_dir_info() -> tuple[Path, str]:
    return (BASE_DIR / BACKEND_DIR_NAME, BACKEND_DIR_NAME)


@pytest.fixture(scope='session')
def dockerfile_name() -> str:
    return DOCKERFILE_NAME


@pytest.fixture(scope='session')
def nginx_dir_info() -> tuple[Path, str]:
    return (BASE_DIR / NGINX_DIR_NAME, NGINX_DIR_NAME)


@pytest.fixture(scope='session')
def expected_nginx_files() -> set[str]:
    return {'nginx.conf', 'Dockerfile'}


@pytest.fixture(scope='session')
def dockerhub_username_key() -> str:
    return DOCKERHUB_USERNAME_KEY


@pytest.fixture
def base_dir() -> Path:
    return BASE_DIR


@pytest.fixture
def workflow_file_name() -> str:
    return WORKFLOW_FILE


@pytest.fixture(scope='session')
def deploy_file_info() -> tuple[Path, str]:
    deploy_info_file = BASE_DIR / DEPLOY_INFO_FILE_NAME
    assert deploy_info_file.is_file(), (
        f'Убедитесь, что в корневой директории проекта создан файл '
        f'`{DEPLOY_INFO_FILE_NAME}`'
    )
    return (deploy_info_file, DEPLOY_INFO_FILE_NAME)


@pytest.fixture(scope='session')
def deploy_info_file_content(
    deploy_file_info: tuple[Path, str],
) -> dict[str, str]:
    path, relative_path = deploy_file_info
    with path.open(encoding='utf-8', errors='ignore') as f:
        file_content = {}
        line_pattern = re.compile(r'[\w_]+: ?[^;]+')
        for line_num, line in enumerate(f.readlines(), 1):
            if not line.strip():
                continue
            assert line_pattern.match(line), (
                f'Убедитесь, что строка номер {line_num} файла '
                f'`{relative_path}` соответствует шаблону: '
                '`<ключ>: <значение>`. В названии ключа '
                'допустимы буквы и нижнее подчеркивание.'
            )
            stripped_line = line.strip().strip(';')
            key, value = stripped_line.split(':', maxsplit=1)
            file_content[key.strip()] = value.strip()
    return file_content


@pytest.fixture(scope='session')
def expected_deploy_info_file_content() -> dict[str, str]:
    return {
        'repo_owner': 'ваше имя пользователя на GitHub',
        TASKI_DOMAIN_KEY: 'ссылка для доступа к проекту `Taski`',
        CATSHARE_DOMAIN_KEY: 'ссылка для доступа к проекту CatShare',
        'dockerhub_username': 'ваше имя пользователя на Docker Hub',
    }


@pytest.fixture(params=(TASKI_DOMAIN_KEY, CATSHARE_DOMAIN_KEY))
def link_key(request) -> str:
    return request.param


@pytest.fixture(scope='session')
def link_keys() -> tuple[str, str]:
    return (CATSHARE_DOMAIN_KEY, TASKI_DOMAIN_KEY)


@pytest.fixture(scope='session')
def catshare_link_key() -> str:
    return CATSHARE_DOMAIN_KEY


@pytest.fixture(scope='session')
def taski_link_key() -> str:
    return TASKI_DOMAIN_KEY
