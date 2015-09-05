from distutils.core import setup
from setuptools import find_packages

setup(
    name='op.common',
    version='0.0.0',
    author='Darwin Monroy',
    author_email='contact@darwinmonroy.com',
    namespace_packages=['op'],
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/dmonroy/op.common',
    description='Open PaaS common utilities',
    install_requires=[
        'anyconfig',
        'attrdict'
    ],
)
