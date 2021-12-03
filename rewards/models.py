from django.db import models


class RewardProgramRegisterHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True)
    reward_program = models.ForeignKey('RewardProgram', on_delete=models.SET_NULL, blank=True, null=True)


class RewardProgram(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    @property
    def latest_version(self):
        return self.version.latest('id')

    def __str__(self):
        return f'{self.name}'


class RewardProgramVersion(models.Model):
    levels = models.JSONField()
    slag = models.CharField(max_length=200, blank=True, null=True)
    reward_program = models.ForeignKey(RewardProgram, on_delete=models.CASCADE, related_name='version')

    def __str__(self):
        return f'{self.id}'
