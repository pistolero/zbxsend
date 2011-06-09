import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "zbxsender",
    version = "0.1",
    author = "Sergey Kirillov",
    author_email = "sergey.kirillov@gmail.com",
    description = ("Module used to send merics to Zabbix."),
    url='https://github.com/pistolero/zbxsend',
    license = "BSD",
#    packages=['zbxstatsd'],
    long_description=read('README.txt'),
#    install_requires=['argparse'],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
#    entry_points={
#        'console_scripts': [
#              'zbx-statsd = zbxstatsd.server:main',
#        ]
#    }
)