from datetime import date, timedelta
from django.test import TestCase

from playground.models import Article, Publisher


class ArticleTestCase(TestCase):

    def setUp(self):
        pass

    def test_added_recently_true(self):

        self.assertTrue(
            Article(
                title='',
                pub_date=date.today() - timedelta(hours=3)
            ).added_recently
        )

    def test_added_recently_false(self):
        self.assertFalse(
            Article(
                title='',
                pub_date=date.today() - timedelta(days=2)
            ).added_recently
        )


class PlaygroundViewTestCase(TestCase):

    def setUp(self):
        publisher = Publisher.objects.create(
            first_name='John',
            last_name='Smith',
            email='john@smith.com'
        )

        for title in map(lambda x: f'Article {x}', range(1000)):
            Article.objects.create(
                title=title,
                pub_date=date.today(),
                publisher=publisher
            )

    def test_index_context(self):
        response = self.client.get('/playground/')

        articles_created = [a for a in Article.objects.all()]
        article_context = [a for a in response.context['articles']]

        return self.assertEqual(articles_created, article_context)
