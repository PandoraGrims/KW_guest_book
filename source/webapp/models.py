from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Book(models.Model):
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Статус", choices=status_choices,
                              default=status_choices[0][0])
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Автор")
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="Мэйл")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.pk} {self.author}"

    class Meta:
        db_table = "books"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
