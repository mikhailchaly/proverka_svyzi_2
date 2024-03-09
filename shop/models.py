from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=50, verbose_name='Менеджер')
    phone = models.CharField(max_length=30, verbose_name="Телефон")
    email = models.CharField(max_length=50, verbose_name="Электронная почта")
    address = models.CharField(max_length=50, verbose_name="Адрес")

    class Meta:
        verbose_name_plural = 'Менеджеры'

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование продукта')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name_plural = 'Продукты'

class Delivery(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата доставки')
    address = models.CharField(max_length=50, verbose_name='Адрес доставки')
    price = models.IntegerField(verbose_name='Цена доставки')

    class Meta:
        verbose_name_plural = 'Доставки'

class OrderState(models.Model):
    name = models.CharField(max_length=50, verbose_name='Статус заказа')

    class Meta:
        verbose_name_plural = 'Статус заказа'

class ClientState(models.Model):
    name = models.CharField(max_length=30, verbose_name='Статус Клиента')

    class Meta:
        verbose_name_plural = 'Статусы Клиентов'

class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='')
    email = models.CharField(max_length=50, verbose_name='')
    phone = models.CharField(max_length=40, verbose_name='')
    state = models.ForeignKey(ClientState, on_delete=models.CASCADE, related_name='clients')


