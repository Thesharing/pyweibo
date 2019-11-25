from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyweibo',
    version='0.1.1',
    packages=['pyweibo'],
    url='https://github.com/Thesharing/pyweibo',
    license='MIT',
    author='Thesharing',
    author_email='',
    description='Python SDK for Weibo API',
    long_description=long_description,
    long_description_content_type='text/markdown',

    install_requires=[
        'spiderutil >= 0.1.6'
    ],

    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],

    python_requires='>=3.4, <4',
)
