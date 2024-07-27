from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    topic = models.ManyToManyField(Topic, through='Scope', verbose_name='Тематика статьи')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='статья')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name='Основной тег')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Тематика статьи'
        ordering = ['-is_main', 'topic']
