from wtforms import Form
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, email, Length


class UserForm(Form):
    email = StringField('email', validators=[DataRequired(message='请输入邮箱！'), email(message='请输入正确格式的邮箱地址！')])
    password = PasswordField('password', validators=[DataRequired(message='请输入密码!'),
                                                   Length(min=4, max=16, message='密码不能小于4位不能大于16位！')])
    remember = IntegerField()
