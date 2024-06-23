from setuptools import setup, find_packages

setup(
    name='my_app_pypi2',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'flask==2.0.1',
        'requests==2.25.1',
    ],
    entry_points={
        'console_scripts': [
            'my_app = my_app.main:main',
        ],
    },
)
