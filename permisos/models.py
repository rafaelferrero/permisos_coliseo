from django.db import models


class Modulo(models.Model):
    padre = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        verbose_name="Ítem de nivel superior",
    )
    nombre = models.CharField(
        max_length=255,
        verbose_name="Nombre del Ítem de menú",
    )
    nombre_completo = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['nombre_completo']

    def __str__(self):
        return "{0}".format(self.nombre_completo)

    def save(self, *args, **kwargs):
        if self.padre is None:
            self.nombre_completo = "{0}".format(self.nombre)
        else:
            self.nombre_completo = "{0}/ {1}".format(self.padre.nombre_completo, self.nombre)
        super(Modulo, self).save(*args, **kwargs)


class Acceso(models.Model):
    permiso = models.ManyToManyField(
        Modulo,
        verbose_name="Modulos permitidos",
        related_name="permiso_acceso",
    )


class Grupo(Acceso):
    nombre = models.CharField(
        max_length=255,
        verbose_name="Nombre del grupo de usuarios",
    )

    def __str__(self):
        return "Grupo {0}".format(self.nombre)


class Usuario(Acceso):
    grupo_usuario = models.ForeignKey(
        Grupo,
        null=True,
        blank=True,
        verbose_name="Grupo de usuarios",
        related_name="grupo_usuario",
    )
    nombre = models.CharField(
        max_length=255,
        verbose_name="Nombre del usuario",
    )

    @property
    def permisos_asignados(self):
        pa = []
        for p in self.permiso.all():
            pa.append({"modulo": p.nombre_completo, "tipo": "U"})
        for p in self.grupo_usuario.permiso.all():
            pa.append({"modulo": p.nombre_completo, "tipo": "G"})
        return pa

    def __str__(self):
        return "{0} - Usuario {1}".format(self.grupo_usuario, self.nombre)
