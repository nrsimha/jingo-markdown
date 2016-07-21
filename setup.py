#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='django-jinja-markdown',
    version="1.0",
    description='Django-Jinja (Jinja2) extension and filter for parse markdown text markup.',
    author='Paul McLanahan',
    author_email='pmac@mozilla.com',
    url='https://github.com/pmac/django-jinja-markdown',
    install_requires=['Markdown'],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Text Processing :: Markup',
    ],
    include_package_data=True,
    zip_safe=False,
)
