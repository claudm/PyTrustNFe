# coding=utf-8
from setuptools import setup, find_packages


VERSION = "1.0.47"


setup(
    name="PyTrustNFe3",
    version=VERSION,
    author="Danimar Ribeiro",
    author_email='danimaribeiro@gmail.com',
    keywords=['nfe', 'mdf-e'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or \
later (LGPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=['*test*']),
    package_data={'pytrustnfe': [
        'nfe/templates/*xml',
        'nfe/fonts/*ttf',
        'nfse/paulistana/templates/*xml',
        'nfse/dsf/templates/*xml',
        'nfse/ginfes/templates/*xml',
        'nfse/simpliss/templates/*xml',
        'nfse/betha/templates/*xml',
        'nfse/susesu/templates/*xml',
        'nfse/imperial/templates/*xml',
        'nfse/floripa/templates/*xml',
        'nfse/carioca/templates/*xml',
        'nfse/bh/templates/*xml',
        'nfse/mga/templates/*xml',
        'nfse/aparecida/templates/*xml',
        'xml/schemas/*xsd',
    ]},
    url='https://github.com/danimaribeiro/PyTrustNFe',
    license='LGPL-v2.1+',
    description='PyTrustNFe é uma biblioteca para envio de NF-e',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'Jinja2 >= 2.8',
        'pyOpenSSL>= 16.0.0, <= 22.0.0',
        'signxml >= 2.21 <= 2.10.1',
        'lxml == 4.9.1',
        'suds-community >= 0.6',
        'reportlab',
        'pytz',
        'zeep',
    ],
    tests_require=[
        'pytest',
    ],
)
