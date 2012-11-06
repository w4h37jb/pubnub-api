import os
import sys
import Pubnub

from setuptools import setup, find_packages

setup(
    name='pubnub',
    version='3.3',
    description='PubNub Real-time push service in the cloud',
    author='Stephen Blum',
    author_email='support@pubnub.com',
    url='https://github.com/downloads/pubnub/pubnub-api/pubnub-3.3-for-pip.tar.gz',
    py_modules=['Pubnub'],
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    zip_safe=False,
)