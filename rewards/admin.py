from django.contrib import admin

from authentication.models import User
from rewards.models import RewardProgramRegisterHistory, RewardProgram, RewardProgramVersion


@admin.register(RewardProgramRegisterHistory)
class RewardProgramRegisterHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'reward_program', 'created_at']


class InlineUserAdmin(admin.TabularInline):
    model = User
    fields = ['reward_program', ]


@admin.register(RewardProgram)
class RewardProgramAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_latest_version', 'show_program_params']
    inlines = [InlineUserAdmin, ]

    def get_latest_version(self, obj):
        return obj.latest_version

    def show_program_params(self, obj):
        return obj.latest_version.levels

    def all_registered_user(self, obj):
        return obj.user.all()

    get_latest_version.short_description = 'last version id'
    show_program_params.short_description = 'level content'


@admin.register(RewardProgramVersion)
class RewardProgramVersion(admin.ModelAdmin):
    list_display = ['id', 'slag', 'reward_program', 'levels']
