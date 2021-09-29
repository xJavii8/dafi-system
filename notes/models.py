from datetime import datetime

from django.db import models

from users.models import User


class NotesCategory(models.Model):

    id: 'models.AutoField[int, int]'

    objects: 'models.Manager[NotesCategory]'

    title: 'models.TextField[str, str]' = models.TextField(
        'título', max_length=128,
    )

    parent: 'models.ForeignKey[NotesCategory | None, NotesCategory | None]' = models.ForeignKey(
        'self', models.CASCADE, related_name='children',
        blank=True, null=True,
        verbose_name='categoría padre'
    )


class NotesType(models.TextChoices):

    THEORY = 'theory'
    EXERCISES = 'exercises'
    PRACTICAL_EXERCISES = 'practical_exercises'
    EXAMS = 'exams'


class Notes(models.Model):

    id: 'models.AutoField[int, int]'

    objects: 'models.Manager[Notes]'

    category: 'models.ForeignKey[NotesCategory, NotesCategory]' = models.ForeignKey(
        NotesCategory, models.CASCADE, related_name='notes',
        verbose_name='categoría'
    )

    user: 'models.ForeignKey[User, User]' = models.ForeignKey(
        User, models.CASCADE, related_name='notes',
        verbose_name='usuario',
    )

    type: 'models.CharField[str, str]' = models.CharField(
        'tipo', choices=NotesType.choices,
        max_length=24
    )

    year: 'models.CharField[str, str]' = models.CharField(
        'curso académico', max_length=8
    )

    file: 'models.FileField' = models.FileField(
        'fichero', upload_to='notes/',
        blank=True, null=True,
    )

    link: 'models.CharField[str, str]' = models.CharField(
        'enlace', max_length=250,
    )

    is_visible: 'models.BooleanField[bool, bool]' = models.BooleanField(
        'es visible', default=False
    )

    created_at: 'models.DateTimeField[datetime, datetime]' = models.DateTimeField(
        'fecha de creación', auto_now_add=True
    )


class AlertTypes(models.TextChoices):

    NEW_NOTES = 'new_notes'
    FEEDBACK = 'feedback'


class Alert(models.Model):

    id: 'models.AutoField[int, int]'

    objects: 'models.Manager[Alert]'

    notes: 'models.ForeignKey[Notes, Notes]' = models.ForeignKey(
        Notes, models.CASCADE, related_name='submission',
        verbose_name='apuntes'
    )

    user: 'models.ForeignKey[User, User]' = models.ForeignKey(
        User, models.CASCADE, related_name='notes_alerts',
        verbose_name='usuario',
    )

    type: 'models.CharField[str, str]' = models.CharField(
        'tipo', choices=AlertTypes.choices,
        max_length=16
    )

    created_at: 'models.DateTimeField[datetime, datetime]' = models.DateTimeField(
        'fecha de creación', auto_now_add=True
    )

    updated_at: 'models.DateTimeField[datetime, datetime]' = models.DateTimeField(
        'última actualización', auto_now=True
    )
