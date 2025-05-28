name = 'jwt_cpp'

version = '0.7.1.hh.1.0.0'

authors = [
    'Dominik Thalhammer',
]

description = '''JWT C++'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']
    c.plugins.release_hook.hh_emailer.recipients = []

requires = [
    "json",
]

private_build_requires = [
]

variants = [
]

def commands():
    env.REZ_JWT_CPP_ROOT = '{root}'
    env.CMAKE_PREFIX_PATH.append('{root}/cmake')
    env.JWT_CPP_INCLUDE_DIR = "{root}/include"

uuid = 'repository.jwt-cpp'
