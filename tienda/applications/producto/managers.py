#Django imports
from django.db import models


class ProductManager(models.Manager):

    def productos_por_user(self, user):
        return self.filter(
            user_created=user,
        )