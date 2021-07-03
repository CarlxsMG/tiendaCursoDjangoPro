#Django imports
from django.db import models


class ProductManager(models.Manager):

    def productos_por_user(self, user):
        return self.filter(
            user_created=user,
        )

    def productos_con_stok(self):
        return self.filter(
            stok__gt=0,
        ).order_by('-num_sales')