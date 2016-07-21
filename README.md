Django-Jinja-Markdown
==============

[Django-Jinja][] ([Jinja2][]) extension and filter to parse markdown text in templates.

Requirements
============

* [Django][] 1.8 or 1.9
* [Django-Jinja][]
* [Python-Markdown][]

[Django]: https://www.djangoproject.com/
[Django-Jinja]: http://niwinz.github.io/django-jinja/latest/ 
[Jinja2]: http://jinja.pocoo.org/
[Python-Markdown]: https://pythonhosted.org/Markdown/

Installation
=============

Install django-jinja-markdown:

    pip install django-jinja-markdown

Add `django_jinja_markdown` to `INSTALLED_APPS`.

To be able to use the `{% markdown %}` tag you should add the Jinja extension 
to your `django_jinja` TEMPLATES extensions list:

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

```jinja
{{ content|markdown }}
{{ markdown('this is **bold**') }}
```

Or with additional settings:

```jinja
{{ content|markdown(extensions=['nl2br',]) }}
{{ markdown(content, extensions=['nl2br',]) }}
```

Example of using extension:

```jinja
{% markdown %}
Text which will get converted with Markdown.
{% endmarkdown %}
```

License
=======

This software is licensed under The MIT License (MIT). For more information, read the file LICENSE.

History
=======

Forked in 2016 from the [jingo-markdown](https://github.com/nrsimha/jingo-markdown) project.
