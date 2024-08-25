# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abonements(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    id_period = models.IntegerField()
    period = models.IntegerField()
    visits = models.IntegerField()
    price = models.IntegerField()
    is_valid = models.TextField()  # This field type is a guess.
    types = models.IntegerField()
    is_start = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'abonements'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Info(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    shir = models.DecimalField(max_digits=8, decimal_places=6)
    dir = models.DecimalField(max_digits=8, decimal_places=6)
    is_valid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'info'


class Lessons(models.Model):
    lesson_day = models.CharField(max_length=3)
    lesson_time = models.CharField(max_length=5)
    is_valid = models.TextField()  # This field type is a guess.
    lesson_date = models.DateField()
    shir = models.DecimalField(max_digits=8, decimal_places=6)
    dir = models.DecimalField(max_digits=8, decimal_places=6)
    description = models.CharField(max_length=400, blank=True, null=True)
    price = models.IntegerField()
    type = models.IntegerField()
    id_trener = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lessons'


class Pays(models.Model):
    user_id = models.IntegerField()
    pay_date = models.DateField()
    summ = models.IntegerField()
    uuid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'pays'


class Periods(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'periods'


class PriceGroups(models.Model):
    id_price = models.IntegerField(blank=True, null=True)
    id_type = models.IntegerField(blank=True, null=True)
    is_valid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'price_groups'


class Reservation(models.Model):
    id_lesson = models.IntegerField()
    date_lesson = models.DateField()
    count_people = models.IntegerField()
    is_valid = models.TextField()  # This field type is a guess.
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'reservation'


class ReservationPeople(models.Model):
    id_people = models.IntegerField()
    id_reservation = models.IntegerField()
    is_valid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'reservation_people'


class Subscriptions(models.Model):
    user_id = models.IntegerField()
    begin_date = models.DateField()
    end_date = models.DateField()
    amount_lessons = models.IntegerField()
    used_lessons = models.IntegerField()
    visited_dates = models.CharField(max_length=255)
    price = models.IntegerField()
    buyed = models.DateField()
    id_abonement = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subscriptions'


class TypeUsers(models.Model):
    type_user = models.PositiveIntegerField(primary_key=True)
    name_user = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    is_valid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'type_users'


class Users(models.Model):
    name = models.CharField(max_length=244)
    phone = models.CharField(max_length=15, blank=True, null=True)
    id_telegram = models.CharField(max_length=255, blank=True, null=True)
    study = models.TextField()  # This field type is a guess.
    oferta = models.TextField()  # This field type is a guess.
    trener = models.TextField()  # This field type is a guess.
    oferta_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersGroups(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_groups'


class Visits(models.Model):
    user_id = models.IntegerField()
    lesson_id = models.IntegerField()
    visit_date = models.DateField()
    trener_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'visits'
