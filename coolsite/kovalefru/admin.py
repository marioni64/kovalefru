from django.contrib import admin
from .models import (
    Abonements,
    AuthGroup,
    AuthGroupPermissions,
    AuthPermission,
    AuthUser,
    AuthUserGroups,
    AuthUserUserPermissions,
    DjangoAdminLog,
    DjangoContentType,
    DjangoMigrations,
    DjangoSession,
    Info,
    Lessons,
    Pays,
    Periods,
    PriceGroups,
    Reservation,
    ReservationPeople,
    Subscriptions,
    TypeUsers,
    Users,
    UsersGroups,
    Visits
)

@admin.register(Abonements)
class AbonementsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'id_period', 'period', 'visits', 'price', 'is_valid', 'types', 'is_start')
    search_fields = ('name', 'description')

@admin.register(AuthGroup)
class AuthGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(AuthGroupPermissions)
class AuthGroupPermissionsAdmin(admin.ModelAdmin):
    list_display = ('group', 'permission')
    list_filter = ('group', 'permission')

@admin.register(AuthPermission)
class AuthPermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'codename')
    search_fields = ('name', 'codename')

@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_superuser', 'is_staff', 'is_active')

@admin.register(AuthUserGroups)
class AuthUserGroupsAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')
    list_filter = ('user', 'group')

@admin.register(AuthUserUserPermissions)
class AuthUserUserPermissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'permission')
    list_filter = ('user', 'permission')

@admin.register(DjangoAdminLog)
class DjangoAdminLogAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'object_id', 'object_repr', 'action_flag', 'change_message', 'content_type', 'user')
    search_fields = ('object_id', 'object_repr', 'change_message')
    list_filter = ('action_flag', 'content_type', 'user')

@admin.register(DjangoContentType)
class DjangoContentTypeAdmin(admin.ModelAdmin):
    list_display = ('app_label', 'model')
    search_fields = ('app_label', 'model')

@admin.register(DjangoMigrations)
class DjangoMigrationsAdmin(admin.ModelAdmin):
    list_display = ('app', 'name', 'applied')
    search_fields = ('app', 'name')

@admin.register(DjangoSession)
class DjangoSessionAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'expire_date')
    search_fields = ('session_key',)

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'shir', 'dir', 'is_valid')
    search_fields = ('name', 'description')

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('lesson_day', 'lesson_time', 'is_valid', 'lesson_date', 'shir', 'dir', 'description', 'price', 'type', 'id_trener')
    search_fields = ('lesson_day', 'lesson_time', 'description')
    list_filter = ('type', 'id_trener')

@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'pay_date', 'summ', 'uuid')
    search_fields = ('user_id', 'uuid')

@admin.register(Periods)
class PeriodsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(PriceGroups)
class PriceGroupsAdmin(admin.ModelAdmin):
    list_display = ('id_price', 'id_type', 'is_valid')
    search_fields = ('id_price', 'id_type')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id_lesson', 'date_lesson', 'count_people', 'is_valid', 'description')
    search_fields = ('id_lesson', 'description')

@admin.register(ReservationPeople)
class ReservationPeopleAdmin(admin.ModelAdmin):
    list_display = ('id_people', 'id_reservation', 'is_valid')
    search_fields = ('id_people', 'id_reservation')

@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'begin_date', 'end_date', 'amount_lessons', 'used_lessons', 'visited_dates', 'price', 'buyed', 'id_abonement')
    search_fields = ('user_id', 'visited_dates', 'id_abonement')

@admin.register(TypeUsers)
class TypeUsersAdmin(admin.ModelAdmin):
    list_display = ('type_user', 'name_user', 'description', 'is_valid')
    search_fields = ('name_user', 'description')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'id_telegram', 'study', 'oferta', 'trener', 'oferta_date')
    search_fields = ('name', 'phone', 'id_telegram')

@admin.register(UsersGroups)
class UsersGroupsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'group_id')
    search_fields = ('user_id', 'group_id')

@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'lesson_id', 'visit_date', 'trener_id')
    search_fields = ('user_id', 'lesson_id')
