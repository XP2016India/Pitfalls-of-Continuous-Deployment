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
    if "staging" not in env.path:
        run("mkdir " + env.path)
    put("sample.tar.gz", env.path)
    with cd(env.path):
        run("tar -zxvf sample.tar.gz")
