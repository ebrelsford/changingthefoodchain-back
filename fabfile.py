import contextlib

from fabric.api import *


env.hosts = ['handthatfeeds',]
env.shell = 'bash --rcfile ~/.bashrc -l -c'
env.use_ssh_config = True

server_project_dirs = {
    'prod': '~/dev---django.thehandthatfeedsfilm.com/public/handthatfeeds/handthatfeeds',
}

server_collected_static = {
    'prod': '~/dev---django.thehandthatfeedsfilm.com/public/static',
}

server_virtualenvs = {
    'prod': 'handthatfeeds',
}

supervisord_programs = {
    'prod': 'handthatfeeds',
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
    with cdstatic(version, ''):
        run('bower install')


@task
def syncdb(version='prod'):
    with workon(version):
        run('django-admin.py syncdb')


@task
def migrate(version='prod'):
    with workon(version):
        run('django-admin.py migrate')


@task
def start(version='prod'):
    pull(version=version)
    install_requirements(version=version)
    syncdb(version=version)
    migrate(version=version)
    build_static(version=version)


@task
def deploy():
    run('echo $DJANGO_SETTINGS_MODULE')
    pull()
    install_requirements()
    syncdb()
    migrate()
    build_static()
