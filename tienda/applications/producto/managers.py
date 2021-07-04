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


    def productos_por_genero(self, genero):
        # Lista productos por genero
        if genero == 'm':
            mujer = True
            varon = False

        elif genero == 'v':
            mujer = True
            varon = False

        else:
            mujer = True
            varon = True

        return self.filter(
            woman=mujer,
            man=varon
        ).order_by('created')