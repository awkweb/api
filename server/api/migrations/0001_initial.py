# Generated by Django 2.0.10 on 2019-03-05 23:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('account_id', models.CharField(max_length=50, verbose_name='account id')),
                ('mask', models.CharField(max_length=4, verbose_name='mask')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('subtype', models.CharField(max_length=50, verbose_name='subtype')),
                ('type', models.CharField(max_length=50, verbose_name='type')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
            options={
                'verbose_name_plural': 'accounts',
                'db_table': 'api_plaid_account',
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('amount_cents', models.IntegerField(verbose_name='amount_cents')),
                ('description', models.CharField(blank=True, max_length=280, verbose_name='description')),
                ('name', models.CharField(max_length=25, verbose_name='name')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
            options={
                'verbose_name_plural': 'budgets',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('institution_id', models.CharField(max_length=50, verbose_name='institution id')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
            options={
                'verbose_name_plural': 'institutions',
                'db_table': 'api_plaid_institution',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('access_token', models.CharField(max_length=200, verbose_name='access token')),
                ('expired', models.BooleanField(default=False, verbose_name='expired')),
                ('item_id', models.CharField(max_length=100, verbose_name='item id')),
                ('public_token', models.CharField(max_length=200, verbose_name='public token')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='api.Institution', verbose_name='institution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'db_table': 'api_plaid_item',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('amount_cents', models.IntegerField(verbose_name='amount cents')),
                ('currency', models.CharField(blank=True, max_length=3, verbose_name='currency')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('description', models.CharField(blank=True, max_length=240, verbose_name='description')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('origin_id', models.CharField(blank=True, max_length=50, verbose_name='origin id')),
                ('origin', models.CharField(choices=[('PL', 'plaid'), ('WI', 'wilbur'), ('VE', 'venmo')], default='WI', max_length=2, verbose_name='origin')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='date deleted')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='api.Account', verbose_name='account')),
                ('budget', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='api.Budget', verbose_name='budget')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='TransactionLocation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('state', models.CharField(max_length=50, verbose_name='state')),
                ('zip', models.CharField(max_length=10, verbose_name='zip')),
                ('lat', models.FloatField(verbose_name='latitude')),
                ('lon', models.FloatField(verbose_name='longitude')),
                ('transaction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_location', to='api.Transaction', verbose_name='transaction')),
            ],
            options={
                'verbose_name': 'transaction location',
                'verbose_name_plural': 'transaction locations',
                'db_table': 'api_transaction_location',
            },
        ),
        migrations.AddIndex(
            model_name='institution',
            index=models.Index(fields=['institution_id'], name='api_plaid_i_institu_6621ff_idx'),
        ),
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='account',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='api.Item', verbose_name='item'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['origin_id'], name='api_transac_origin__010846_idx'),
        ),
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['item_id'], name='api_plaid_i_item_id_04031d_idx'),
        ),
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['account_id'], name='api_plaid_a_account_85281d_idx'),
        ),
    ]
