from django.db import models


class SubjectCategory(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    image = models.ImageField('Обложка', upload_to='static/img/catalog', height_field=None, width_field=None, max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class Books(models.Model):
    WithoutIndustry = 'wi'
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
        (WithoutIndustry, 'Без отрасли'),
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
    avtordesc = models.TextField(blank=True)
    pages = models.IntegerField(default=0)
    format = models.CharField(max_length=2, choices=FORMAT_CHOICES, default=AUDIO)
    industries = models.CharField(max_length=2, choices=INDUSTRIES_CHOICES, default=WithoutIndustry, blank=True)
    document = models.FileField(upload_to='media/book/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    bookimage = models.ImageField('Обложка книги', upload_to='static/img/book', height_field=None, width_field=None, max_length=100,
                              null=True)
    avtorphoto = models.ImageField('Фото автора', upload_to='static/img/avtor', height_field=None, width_field=None, max_length=100,
                              null=True)



    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Personality(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    photo = models.ImageField('Личность', upload_to='static/img/personality', height_field=None, width_field=None, max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Личность'
        verbose_name_plural = 'Личности'