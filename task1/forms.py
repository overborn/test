# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import IntegerField, SelectField
from wtforms.validators import InputRequired


class IndexForm(Form):
    car = SelectField(u'Выберите производителя:',
                      choices=[],
                      validators=[InputRequired()])
    model = SelectField(u'Выберите модель:',
                        choices=[],
                        validators=[InputRequired()])
    run = IntegerField(u'Введите пробег в км.:', validators=[InputRequired()])
