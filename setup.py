# encoding: utf-8

"""
mana
-------------

my flask toolkit,  help me generate my flask app.
"""
from setuptools import setup, find_packages


setup(
    name='mana0',
    version='0.11',
    packages=find_packages(),
    url='https://github.com/neo1218/mana',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='my flask toolkit',
    long_description=__doc__,
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        mana0=mana0.mana.mana:mana
    ''',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
