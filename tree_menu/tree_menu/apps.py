from django.apps import AppConfig


class TreeMenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tree_menu'

    def ready(self):
        from django.core.exceptions import ValidationError
        from django.db.models.signals import pre_save
        from django.dispatch import receiver

        from .models import MenuItem

        @receiver(pre_save, sender=MenuItem)
        def validate_parent(sender, instance, *args, **kwargs):
            """
            Сигнал проверяет, что main_menu у родительского элемента совпадает
            с main_menu текущего элемента.
            """
            if (
                instance.parent and instance.parent.main_menu !=
                instance.main_menu
            ):
                raise ValidationError(
                    "Выберите другое родительское меню. Родитель должен иметь "
                    "то-же главное древовидное меню, что и объект.")
