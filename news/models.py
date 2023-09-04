from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_image')
    created_time = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.title}'
