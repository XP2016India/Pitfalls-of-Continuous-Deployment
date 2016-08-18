import os
from fabric.api import *

def production():
    build_number = os.environ['BUILD_NUMBER']
    env.hosts = ['xpconf@localhost']
    env.path = '/home/xpconf/websites/sample-live-{}'.format(build_number)

def staging():
    env.hosts = ['xpconf@localhost']
    env.path = '/home/xpconf/websites/sample-staging'

def deploy():
    if "staging" in env.path:
        with cd(env.path):
            run("rm sample/ -rf")
    else:
        run("mkdir " + env.path)
    put("sample.tar.gz", env.path)
    with cd(env.path):
        run("tar -zxvf sample.tar.gz")
    if "staging" in env.path:
        run("supervisorctl restart staging")
    else:
        run("rm /home/xpconf/websites/sample-live")
        run("ln -s {} /home/xpconf/websites/sample-live".format(env.path))
        run("supervisorctl restart live")
