import os

from django.core.validators import ValidationError


def get_path_upload_avatar(instance, file):
    """ Построение пути к файлу, format: (media)/profile/user_id/photo.jpg """

    return f"profile/user_{instance.id}/{file}"


def get_path_upload_post_image(instance, file):
    """ Построение пути к файлу, format: (media)/profile/user_id/photo.jpg """

    return f"profile/user_{instance.id}/{file}"


def product_image_directory_path(instance, filename):
    """ Построение пути к медиа файлам поста пользователя (media)/profile/user_id/posts/photo.jpg """

    return f"profile/user_{0}/posts/{1}.jpg".format(instance.id, filename)


def validate_size_image(file_object):
    """ Проверка размера загружаемого файла """

    megabyte_limit = 2
    if file_object.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла не должен превышать {megabyte_limit}MB")


def get_path_upload_track(instance, file):
    """ Построение пути к файлу, format: (media)/track/user_id/photo.jpg """

    return f"track/user_{instance.user.id}/{file}"


def get_path_upload_picture_track(instance, file):
    """ Построение пути к файлу, format: (media)/track/picture/user_id/photo.jpg """

    return f"track/picture/user_{instance.user.id}/{file}"


def get_path_upload_picture_album(instance, file):
    """ Построение пути к файлу, format: (media)/album/user_id/photo.jpg """

    return f"album/user_{instance.user.id}/{file}"


def get_path_upload_picture_playlist(instance, file):
    """ Построение пути к файлу, format: (media)/playlist/user_id/photo.jpg """

    return f"playlist/user_{instance.user.id}/{file}"


def get_path_upload_group_community_image(instance, file):
    """ Построение пути к файлу, format: (media)/groups/group_id/community_image/photo.jpg """

    return f"groups/group_{instance.id}/community_image/{file}"


def get_path_upload_group_background_image(instance, file):
    """ Построение пути к файлу, format: (media)/groups/group_id/background_image/photo.jpg """

    return f"groups/group_{instance.id}/background_image/{file}"


def get_path_upload_group_article_image(instance, file):
    """ Построение пути к файлу, format: (media)/groups/group_id/article/photo.jpg """

    return f"groups/group_{instance.id}/article/{file}"


def delete_old_file(path_file):
    """ Удаление старого файла """

    if os.path.exists(path_file):
        os.remove(path_file)