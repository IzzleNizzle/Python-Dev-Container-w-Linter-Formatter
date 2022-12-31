from setuptools import setup, find_packages

setup(
    name='app',
    version='0.1.1',
    license='proprietary', 
    description='TDD Template in python',
    packages=find_packages(where='app'),
    package_dir={'': 'app'},
    install_requires=['pytest', 'pytest-mock'],
    tests_require=['pytest', 'pytest-mock'],
)
