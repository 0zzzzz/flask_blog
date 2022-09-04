import os
from secrets import token_hex
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from oz_blog import mail
from oz_blog.config import Config


def save_picture(form_picture):
    random_hex = token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    """Отправка письма для восстановления пароля"""
    token = user.get_reset_token()
    msg = Message('Сброс пароля',
                  sender=Config.MAIL_USERNAME,
                  recipients=[user.email])
    msg.body = f'Вы запросили восстановление пароля на oz_blog \n' \
               f'Для продолжения перейдите по ссылке — старый пароль сбросится, останется только задать новый:\n' \
               f'{url_for("users.reset_token", token=token, _external=True)}\n' \
               f'Если вы не запрашивали восстановление пароля или вдруг передумали,\n' \
               f'проигнорируйте это письмо, мы сохраним старый пароль для входа '
    mail.send(msg)
