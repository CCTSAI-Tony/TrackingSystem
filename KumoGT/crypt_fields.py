from io import BytesIO

from django.urls import reverse
from django.db.models.fields.files import (
    FieldFile,
    FileField,
    ImageField,
    ImageFieldFile
)

from .crypt import Cryptographer

from urllib.parse import quote as url_encode 


class EncryptedFile(BytesIO):
    def __init__(self, content):
        self.size = content.size
        BytesIO.__init__(self, Cryptographer.encrypted(content.file.read()))


class EncryptionMixin(object):

    def save(self, name, content, save=True):
        return FieldFile.save(
            self,
            name,
            EncryptedFile(content),
            save=save
        )
    save.alters_data = True

    def _get_url(self):
        return reverse('documents/', kwargs={
            "path": super(EncryptionMixin, self).url
        })
    url = property(_get_url)


class EncryptedFieldFile(EncryptionMixin, FieldFile):
    pass


class EncryptedImageFieldFile(EncryptionMixin, ImageFieldFile):
    pass


class EncryptedFileField(FileField):
    attr_class = EncryptedFieldFile


class EncryptedImageField(ImageField):

    attr_class = EncryptedImageFieldFile

    def update_dimension_fields(self, instance, force=False, *args, **kwargs):
        """
        Since we're encrypting the file, any attempts to force recalculation of
        the dimensions will always fail, resulting in a null value for height
        and width.  To avoid that, we just set force=False all the time and
        expect that if you want to change those values, you'll do it on your
        own.
        """
        ImageField.update_dimension_fields(
            self, instance, force=False, *args, **kwargs)
