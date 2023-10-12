import pytest
from dbtemplates.models import Template
from faker import Faker
from rest_framework.test import APIClient

from df_documents.models import Document

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "md_content, html_content",
    [
        ("# Hello", "<h1>Hello</h1>"),
    ],
)
def test_retrieve_document(
    md_content: str, html_content: str, faker: Faker, client: APIClient
) -> None:
    slug = faker.slug()
    Document.objects.create(slug=slug, content=md_content)

    response = client.get(f"/legal/{slug}/")

    assert response.status_code == 200
    assert response.content.decode().strip() == html_content


@pytest.mark.parametrize(
    "md_content, html_content, template",
    [
        ("## Hello", "<h2>Hello</h2>", "<h1>header</h1>"),
    ],
)
def test_retrieve_document_with_template_extend(
    md_content: str, html_content: str, template: str, faker: Faker, client: APIClient
) -> None:
    template_name = "base.html"
    md_content = f"""
{{% extends 'base.html' %}}

{{% block content %}}
{md_content}
{{% endblock %}}
"""
    template_content = f"""
{template}
{{% block content %}}
{{% endblock %}}
"""
    slug = faker.slug()
    Template.objects.create(name=template_name, content=template_content)
    Document.objects.create(slug=slug, content=md_content)

    response = client.get(f"/legal/{slug}/")

    assert response.status_code == 200
    assert html_content in response.content.decode().strip()
    assert template in response.content.decode().strip()
