from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва кафедри")
    head = models.CharField(max_length=200, verbose_name="Завідувач кафедри")

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва спеціальності")
    code = models.CharField(max_length=20, verbose_name="Код спеціальності")
    description = models.TextField(verbose_name="Опис спеціальності")
    coordinator_name = models.CharField(max_length=200, verbose_name="Ім'я координатора набору")
    coordinator_contact = models.CharField(max_length=200, verbose_name="Контакт координатора набору")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs', verbose_name="Випускова кафедра")
    disciplines = models.TextField(verbose_name="Список дисциплін")

    def __str__(self):
        return f"{self.name} ({self.code})"

class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я викладача")
    position = models.CharField(max_length=200, verbose_name="Посада")
    degree = models.CharField(max_length=200, verbose_name="Науковий ступінь")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers', verbose_name="Кафедра")

    def __str__(self):
        return self.name

class MainPageContent(models.Model):
    content = models.TextField(verbose_name="Текст головної сторінки")

    def __str__(self):
        return "Текст головної сторінки"
