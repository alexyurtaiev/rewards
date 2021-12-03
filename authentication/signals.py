from django.db.models.signals import pre_save
from django.dispatch import receiver

from authentication.models import User
from rewards.models import RewardProgramRegisterHistory


@receiver(pre_save, sender=User)
def save_historical_data(sender, instance: User, **kwargs):
    user = User.objects.filter(id=instance.id)
    if user.exists():
        historical_data = RewardProgramRegisterHistory(
            user=instance,
            reward_program=instance.reward_program,
        )
        historical_data.save()