import contextlib

from fabric.api import *


env.hosts = ['ctfc',]
env.shell = 'bash --rcfile ~/.bashrc -l -c'
env.use_ssh_config = True

server_project_dirs = {
    'prod': '~/webapps/fcwaapi/changingthefoodchain-back',
}

server_collected_static = {
    'prod': '~/webapps/ctfc_static',
}

server_virtualenvs = {
    'prod': 'fcwaapi',
}

supervisord_programs = {
    'prod': 'ctfc',
}

supervisord_conf = '~/var/supervisor/supervisord.conf'


@contextlib.contextmanager
def cdversion(version, subdir=''):
    """cd to the version indicated"""
    with prefix('cd %s' % '/'.join([server_project_dirs[version], subdir])):
        yield


@contextlib.contextmanager
def cdstatic(version, subdir=''):
    """cd to the version indicated"""
    with prefix('cd %s' % '/'.join([server_collected_static[version], subdir])):
        yield


@contextlib.contextmanager
def workon(version):
    """workon the version of indicated"""
    with prefix('workon %s' % server_virtualenvs[version]):
        yield

@task
def pull(version='prod'):
    with cdversion(version):
        run('git pull')


@task
def install_requirements(version='prod'):
    with workon(version):
        with cdversion(version):
            run('pip install -r requirements/base.txt')
            run('pip install -r requirements/production.txt')


@task
def build_static(version='prod'):
    with workon(version):
        run('django-admin.py collectstatic --noinput')
    with cdstatic(version, ''):
        run('npm install')


@task
def syncdb(version='prod'):
    with workon(version):
        run('django-admin.py syncdb')


@task
def migrate(version='prod'):
    with workon(version):
        run('django-admin.py migrate')


@task
def restart_django(version='prod'):
    with workon(version):
        run('supervisorctl --config %s restart %s' % (
            supervisord_conf,
            supervisord_programs[version],
        ))


@task
def start(version='prod'):
    pull(version=version)
    install_requirements(version=version)
    syncdb(version=version)
    migrate(version=version)
    build_static(version=version)


@task
def deploy():
    pull()
    install_requirements()
    syncdb()
    migrate()
    build_static()
    restart_django()
