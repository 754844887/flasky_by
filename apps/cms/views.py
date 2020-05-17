from flask import Blueprint, request, render_template, session
from .form import UserForm
from .models import User

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('cms/login.html', errors='')
    else:
        form = UserForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(raw_password=password):
                session['username'] = user.id
                if remember:
                    session.permanent = True
                return 'login'
            else:
                return '密码错误'
        else:
            errors = form.errors
            return render_template('cms/login.html', errors=errors)
