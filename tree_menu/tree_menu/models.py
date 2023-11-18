from django.db import models


class Menu(models.Model):
    """
    Модель создана, для названий древовидных меню, что-бы все пункты одного
    древовидного меню можно было получить с помощью одного запроса к БД.
    """

    name = models.CharField(
        'Название древовидного меню',
        max_length=100, unique=True
    )

    class Meta:
        verbose_name = 'Название древовидного меню'
        verbose_name_plural = 'Название древовидного меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Модель для древовидных меню."""

    name = models.CharField('Название меню', max_length=100, unique=True)
    url = models.SlugField('url-адрес', max_length=200, unique=True)
    parent = models.ForeignKey(
        'self', blank=True, null=True, verbose_name='Родительское меню',
        related_name='children', on_delete=models.CASCADE
    )
    main_menu = models.ForeignKey(
        to=Menu, verbose_name='Название древовидного меню',
        related_name='main_menus', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Древовидное меню'
        verbose_name_plural = 'Древовидное меню'

    def __str__(self):
        return self.name
