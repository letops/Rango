from easy_thumbnails.files import get_thumbnailer
import os


def avatarFile(instance, filename):
    name, ext = os.path.splitext(filename)
    return "avatars/%s-%s%s" % (instance.username, name[:3], ext)


# Get fields from instances for lists
def clean_field_value(instance, field):
    if field.name == 'photo':
        return get_thumbnailer(instance.photo)['preview_smallest'].url
    elif field.name == 'qr':
        return get_thumbnailer(instance.qr)['preview_smallest'].url
    elif field.name.startswith('datetime'):
        return instance._get_FIELD_display(field)
    else:
        return field.value_to_string(instance)[:70]


def get_instance_field_headers(instance):
    return [field.verbose_name for field in instance.get_list_fields()]


def get_instance_fields(instance, list_headers=None):
    list_headers = list_headers if list_headers is not None else instance.get_list_fields()
    return [(field.name, clean_field_value(instance, field)) for field in list_headers]