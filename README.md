jingo-markdown
==============

Jingo (Jinja2) extension and filter for parse markdown text markup.


Requirements
============

Python-Markdown - http://packages.python.org/Markdown/


Installation
=============

Install jingo-markdown:

    pip install jingo-markdown

Add 'jingo_markdown' to INSTALLED_APPS.

To be able to use `markdown` extension you should add it to JINJA_CONFIG extensions list:

JINJA_CONFIG = {
    'extensions': [
        'jingo_markdown.extensions.MarkdownExtension',
    ]
}


Basic Use
=========

Example of using filter in template:

    {{ content|markdown() }}

Or with additional settings:

    {{ content|markdown(extensions=['nl2br',]) }}

Example of using extension:

    {% markdown %}
    Text which will get converted with Markdown.
    {% endmarkdown %}

License
=======

This software is licensed under The MIT License (MIT). For more information, read the file LICENSE.