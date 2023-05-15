from flask_script import Manager, Command
from flask import Flask

app = Flask(__name__)

manager = Manager(app)


# 第一种
@manager.command
def greet():
    print("你好")


# 第二种
class Hello(Command):
    def run(self):
        print("hello")


# 第三种
@manager.option('-n','--name', dest='name')
def hi(name):
    print("hi {}".format(name))


manager.add_command('hello', Hello())


if __name__ == '__main__':
    manager.run()