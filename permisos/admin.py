from django.contrib import admin
from permisos.models import (
    Modulo,
    Grupo,
    Usuario,
)


@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    pass


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    pass


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
