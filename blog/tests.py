from django.test import TestCase, Client
from django.urls import reverse
from .models import Author, Post, Tag
from datetime import date


class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Joan",
            last_name="Garcia",
            email="joan@example.com"
        )

    def test_author_creation(self):
        self.assertEqual(self.author.first_name, "Joan")
        self.assertEqual(self.author.last_name, "Garcia")

    def test_author_str(self):
        self.assertEqual(str(self.author), "Joan Garcia")


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(caption="django")

    def test_tag_creation(self):
        self.assertEqual(self.tag.caption, "django")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "django")

    def test_tag_unique(self):
        with self.assertRaises(Exception):
            Tag.objects.create(caption="django")


class PostModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Joan",
            last_name="Garcia",
            email="joan@example.com"
        )
        self.post = Post.objects.create(
            title="Post de prova",
            excerpt="Aquest és un excerpt de prova",
            image_name="test.jpg",
            date=date(2024, 1, 1),
            slug="post-de-prova",
            content="Aquest és el contingut de prova del post.",
            author=self.author
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Post de prova")
        self.assertEqual(self.post.slug, "post-de-prova")

    def test_post_str(self):
        self.assertEqual(str(self.post), "Post de prova")


class UrlTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(
            first_name="Joan",
            last_name="Garcia",
            email="joan@example.com"
        )
        self.post = Post.objects.create(
            title="Post de prova",
            excerpt="Aquest és un excerpt de prova",
            image_name="test.jpg",
            date=date(2024, 1, 1),
            slug="post-de-prova",
            content="Aquest és el contingut de prova del post.",
            author=self.author
        )

    def test_starting_page(self):
        response = self.client.get(reverse("starting-page"))
        self.assertEqual(response.status_code, 200)

    def test_posts_page(self):
        response = self.client.get(reverse("posts-page"))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_page(self):
        response = self.client.get(reverse("post-detail-page", args=["post-de-prova"]))
        self.assertEqual(response.status_code, 200)

    def test_authors_page(self):
        response = self.client.get(reverse("authors-page"))
        self.assertEqual(response.status_code, 200)

    def test_tags_page(self):
        response = self.client.get(reverse("tags-page"))
        self.assertEqual(response.status_code, 200)