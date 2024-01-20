from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


# Create your models here.


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _('Image')
        VIDEO = 'video', _('Video')
        AUDIO = 'audio', _('Audio')
        DOCUMENT = 'document', _('Document')
        GIF = 'gif', _('Gif')
        OTHER = 'other', _('Other')

    file = models.FileField(upload_to='only_medias/', verbose_name=_("File"),
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi',
                                                                                   'mov', 'mp3', 'doc', 'docx', 'xls',
                                                                                   'xlsx', 'ppt', 'pptx', 'txt', 'csv',
                                                                                   'zip', 'rar', 'webp', 'gif',
                                                                                   'wav'])])
    file_type = models.CharField(max_length=10, verbose_name=_("File type"), choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Medias")

    def __str__(self):
        return f"File id: {self.id}"

    # Automatic choice of extension file
    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'avi', 'mov']:
                raise ValidationError(_("Invalid Video File"))
        elif self.file_type == self.FileType.AUDIO:
            if self.file.name.split('.')[-1] not in ['mp3', 'wav']:
                raise ValidationError(_("Invalid Audio File"))
