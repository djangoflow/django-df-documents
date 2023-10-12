import markdown
from django.db import models
from django.template import Template, Context
import re


class Document(models.Model):
    slug = models.SlugField(unique=True)
    content = models.TextField(
        help_text="Markdown. First line could be {% extends 'xxxxxxx.html' %}"
    )

    def render_to_html(self):
        content_html = markdown.markdown(self.content.strip())
        content_html = re.sub(r"<p>\{%(.+?)%}</p>", r"{%\1%}", content_html)
        return Template(content_html).render(Context({}))

    def __str__(self):
        return self.slug
