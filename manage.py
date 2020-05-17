from flask_script import Manager
from myapp import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
from apps.cms.models import User


manager = Manager(app)
# 1. 要使用flask_migrate，必须绑定app和db
migrate = Migrate(app, db)
# 2. 把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--user', dest='username')
@manager.option('-e', '--email', dest='email')
@manager.option('-p', '--password', dest='password')
def create_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    print('创建用户成功!')

if __name__ == '__main__':
    manager.run()