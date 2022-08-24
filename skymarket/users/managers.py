from django.contrib.auth.models import (
    BaseUserManager
)


# менеджер для модели Юзера.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None):
        """Создание и запись пользователя с использованием email и пароля"""
        if not email:
            raise ValueError('Users nust have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
        user.role = 'user',
        user.is_active = True,
        user.set_password(password),
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """Создание и запись суперпользователя"""
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
        user.role = 'admin',
        user.save(using=self._db)
        return user
