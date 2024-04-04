from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length



class ReviewForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(message="Поле не должно быть пустым"),
                                                Length(max=255, message='Введите заголовок длиной до 255 символов')])
    text = TextAreaField('Текст', validators=[DataRequired(message="Поле не должно быть пустым")])
    submit = SubmitField('Добавить')