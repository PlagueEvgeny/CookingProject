from django.db import models


class SubjectCategory(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class Books(models.Model):
    War = 'w'
    Cultural = 'c'
    Science = 's'
    Right = 'r'
    Political = 'p'
    Religion = 're'
    Economics = 'e'
    AUDIO = 'a'
    TEXT = 't'
    ELECTRONIC = 'el'

    INDUSTRIES_CHOICES = (
        (War, 'Военная история'),
        (Cultural, 'История культуры'),
        (Science, 'История науки'),
        (Right, 'История государства и права '),
        (Political, 'История политических и правовых учений'),
        (Religion, 'История религии'),
        (Economics, 'История экономики'),

    )
    FORMAT_CHOICES = (
        (AUDIO, "Аудио формат"),
        (TEXT, "Бумажный формат"),
        (ELECTRONIC, "Электронный формат"),
    )

    category = models.ForeignKey(SubjectCategory,
                                 on_delete=models.CASCADE)
    # slug = models.SlugField()  # name -> some function -> slug
    name = models.CharField(max_length=200)
    avtor = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    pages = models.IntegerField(default=0)
    format = models.CharField(max_length=2, choices=FORMAT_CHOICES, default=AUDIO)
    industries = models.CharField(max_length=2, choices=INDUSTRIES_CHOICES, default=War)



    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'