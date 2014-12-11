#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='jingo-markdown',
    version="1.3",
    description='Jingo (Jinja2) extension and filter for parse markdown text markup.',
    author='Prahlad Nrsimha Das - Petr Vacha',
    author_email='pnd@mayapurmedia.com',
    url='https://github.com/mayapurmedia/jingo-markdown',
    install_requires=['Markdown'],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Text Processing :: Markup',
    ],
    include_package_data=True,
    zip_safe=False,
)
