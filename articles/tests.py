from django.test import TestCase
from django.urls import reverse
from .models import Article, Comment
from django.contrib.auth import get_user_model


# Create your tests here.

class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.article = Article.objects.create(
            title='Test Article',
            summary='Test Summary',
            body='Test Body',
            author=self.user
        )
        Comment.objects.create(
            article=self.article,
            comment='Test Comment',
            author=self.user
        )

    def test_article_model(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.summary, 'Test Summary')
        self.assertEqual(self.article.body, 'Test Body')
        self.assertEqual(self.article.author, self.user)

    def test_comment_model(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.comment, 'Test Comment')
        self.assertEqual(comment.article, self.article)
        self.assertEqual(comment.author, self.user)

    def test_article_absolute_url(self):
        url = reverse('article_detail', args=[str(self.article.id)])
        self.assertEqual(url, '/articles/' + str(self.article.id))

    def test_comment_absolute_url(self):
        url = reverse('article_list')
        self.assertEqual(url, '/articles/')
