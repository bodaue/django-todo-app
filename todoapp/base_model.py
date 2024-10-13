from django.db.models import Manager, Model


class BaseModel(Model):
    objects = Manager()

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self._meta.verbose_name} №{self.pk}"
