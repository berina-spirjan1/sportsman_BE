# Generated by Django 4.2 on 2023-05-01 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsman', '0002_rename_users_user_rename_usertypes_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('location', models.TextField(null=True)),
                ('tel_number', models.CharField(max_length=20, null=True)),
                ('capacity', models.IntegerField(null=True)),
                ('type', models.IntegerField(null=True)),
                ('picture', models.CharField(max_length=50, null=True)),
                ('typeOfUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportsman.usertype')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tel_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Team_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsman.team')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsman.user')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='team_lead_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sportsman.user'),
        ),
        migrations.CreateModel(
            name='Sport_hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.TextField(null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('price', models.FloatField()),
                ('pictures', models.TextField(null=True)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsman.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Permanent_teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsman.team')),
            ],
        ),
        migrations.CreateModel(
            name='Invitations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sent', models.DateTimeField(null=True)),
                ('status', models.IntegerField()),
                ('details', models.TextField(null=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_invitations', to='sportsman.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_invitations', to='sportsman.user')),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=50)),
                ('status', models.IntegerField()),
                ('time_appointed', models.DateTimeField(null=True)),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsman.team')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends1', to='sportsman.user')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends2', to='sportsman.user')),
            ],
        ),
    ]
