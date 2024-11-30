from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Asignacion

@receiver(post_save, sender=Asignacion)
def enviar_notificacion(sender, instance, created, **kwargs):
    if created:
        print(f"Notificación: Asignación {instance.id_asignacion} creada.")