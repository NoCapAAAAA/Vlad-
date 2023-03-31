from django.core.exceptions import ValidationError


def validate_phone_number(phone):
    allowed_chars = '+1234567890'
    for i in phone:
        if i not in allowed_chars:
            raise ValidationError('Номер телефона может содержать лишь цифры')

        elif len(phone) >= 12:
            raise ValidationError('Слишком длинный у тебя *****')
        elif len(phone) <= 10:
            raise ValidationError('Слишком короткий у тебя *****')

def validate(name):
    allowed_chars = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ  !@#$%^&*!"":''1234567890-(),./?><|][]}{;№;%:?* \n")
    for i in name:
        if i not in allowed_chars:
            raise ValidationError('Данное поле может содержать лишь символы Лантици и Криллицы')