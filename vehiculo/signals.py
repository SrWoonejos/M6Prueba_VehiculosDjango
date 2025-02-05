from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

@receiver(post_save, sender=User)
def asignar_permiso_visualizar_catalogo(sender, instance, created, **kwargs):
    if created:  # Solo al crear un usuario nuevo
        permiso = Permission.objects.get(codename="visualizar_catalogo")
        instance.user_permissions.add(permiso)
