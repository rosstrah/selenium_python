import os
import re

from setuptools import find_packages, setup


REGEXP = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")


def read_version():

    init_py = os.path.join(os.path.dirname(__file__), 'main', '__init__.py')

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f'Cannot find version in ${init_py}'
            raise RuntimeError(msg)


install_requires = [
    'aiohttp==3.7.3',
    'aiopg==0.14.0',
]


setup(
    name='main',
    version=read_version(),
    description='main modul',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    #install_requires=install_requires,
    zip_safe=False,
)