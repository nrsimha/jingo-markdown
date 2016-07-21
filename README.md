django-jinja-markdown
==============

django-jinja (Jinja2) extension and filter for parse markdown text markup.


Requirements
============

Python-Markdown - http://packages.python.org/Markdown/


Installation
=============

Install django-jinja-markdown:

    pip install django-jinja-markdown

Add 'django_jinja_markdown' to INSTALLED_APPS.

To be able to use `markdown` extension you should add it to TEMPLATES extensions list:

```python
TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'OPTIONS': {
            'extensions': [
                'django_jinja_markdown.extensions.MarkdownExtension',
            ],
        }
    },
]
```

Basic Use
=========

Examples of using filter in template:

    {{ content|markdown }}
    {{ markdown('this is **bold**') }}

Or with additional settings:

    {{ content|markdown(extensions=['nl2br',]) }}
    {{ markdown(content, extensions=['nl2br',]) }}

Example of using extension:

    {% markdown %}
    Text which will get converted with Markdown.
    {% endmarkdown %}

License
=======

This software is licensed under The MIT License (MIT). For more information, read the file LICENSE.
