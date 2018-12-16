from setuptools import setup



# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()



setup(
    name='visitoolkit-connector',
    version='0.1.2',
    packages=['visitoolkit_connector'],
    install_requires=['visitoolkit-eventsystem==0.1.5',
                      'websocket-client-py3==0.15.0',
                      'python-dateutil==2.7.3'],
    url='https://github.com/stefanbraun-private/visitoolkit_connector',
    license='GPL-3.0',
    author='Stefan Braun',
    author_email='sbraun@datacomm.ch',
    description='client implementation of "DMS JSON Data Exchange v1.4"',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
