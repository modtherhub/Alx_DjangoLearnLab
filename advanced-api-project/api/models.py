from django.db import models

class Author(models.Model):
    """
    نموذج لتخزين بيانات المؤلف.
    يحتوي على اسم المؤلف فقط.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    نموذج لتخزين بيانات الكتاب.
    يحتوي على العنوان وسنة النشر، ويرتبط بمؤلف عبر مفتاح أجنبي.
    """
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
