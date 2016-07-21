from django.template import engines
from django.test import TestCase


engine = engines.all()[0]


class TestDjangoJinjaMarkdown(TestCase):
    def test_markdown_filter(self):
        self.assertEqual(engine.from_string('{{ "**bold dude**"|markdown }}').render(),
                         '<p><strong>bold dude</strong></p>')

    def test_markdown_function(self):
        self.assertEqual(engine.from_string('{{ markdown("***angry walter***") }}').render(),
                         '<p><strong><em>angry walter</em></strong></p>')

    def test_markdown_tag(self):
        self.assertEqual(engine.from_string('{% markdown %}*fancy donnie*{% endmarkdown %}').render(),
                         '<p><em>fancy donnie</em></p>')
