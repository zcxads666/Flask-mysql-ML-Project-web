import numpy as np
from flask import Flask, request, render_template
import pickle
from datetime import timedelta
import pymysql
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

app.config['SEND_FILE_MAX_AGE_DEFAULT']=timedelta(seconds=1) # 设置为10秒

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/db1'
#后端显示页'mysql+pymysql://{数据库账户名}:{密码}@{地址/本地就不用改}:{端口，默认3306不用改}/{使用的数据库名}'

db = SQLAlchemy(app)
admin = Admin(app, name='admin', template_mode='bootstrap3')


class user(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80), unique=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    from flask_admin.contrib.sqla import ModelView


    class CustomUserView(ModelView):
        # 指定要显示的列
        column_list = ('name', 'password')




    admin.add_view(CustomUserView(user, db.session))






@app.route("/")
def Home():
    return render_template("log.html")

@app.route('/det')
def det():
    return render_template("index.html")

@app.route('/res')
def loginHome():
    return render_template("res2.html")

@app.route('/evaluate')
def eva():
    return render_template("evaluate.html")

@app.route('/author')
def auth():
    return render_template("author.html")


# 定义一个预测路由，以post方式提交数据
@app.route("/predict", methods = ["POST"])

def predict():
    float_features = [float(x) for x in list(request.form.values())[:11]]
    features = [np.array(float_features)]

#预测模型结果
    prediction = model.predict(features)[0]

    return render_template("index.html", prediction_text="count：{}".format(prediction))



def get_conn():
    # 建立与mysql连接
    conn = pymysql.connect(host="localhost", user="root", password="root", db="db1", charset="utf8")#修改为你自己的数据库信息
    #host="localhost"本地的数据库这个不用改, user="你的登录账户名", password="你的密码", db="使用的数据库名称"
    # c创建游标A
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):  # 关闭模块
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):  # 查询模块

    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    conn.commit()
    close_conn(conn, cursor)
    return res


@app.route('/login', methods=['post'])
def login():
    username = request.form.get('username')  # 接收form表单传参
    password = request.form.get('password')
    res = get_user(username, password)
    if res:
        return render_template('index.html', msg='登陆成功')
    else:
        return render_template('log.html', msg='登录失败')

@app.route('/resgin', methods=['post'])
def resgin():
    username = request.form.get('username')  # 接收form表单传参
    password = request.form.get('password')
    res = get_user(username, password)
    if res:
        return render_template('res2.html', msg='注册失败,重复账户')
    else:
        res2 = input_user(username, password)
        print(username, password)
        print(res2)
        if res2:
            return render_template('log.html', msg='注册成功')
        else:
            return render_template('res2.html', msg='注册失败')
def get_user(username, password):  # 从数据库中查询用户名和密码
    # username=str(username)
    # password=str(password)
    print(username + " " + password)
    sql = "select * from user where name= '" + username + "' and password= '" + password + "'"
    #修改为你表里面的参数 select * from {表名} where {存放用户字段名}= '" + username + "' and {存放密码字段名}= '" + password + "'"
    res = query(sql)

    return res

def input_user(username, password):
    # username=str(username)
    # password=str(password)
    print(username + " " + password)
    sql = "INSERT INTO user(name, password) VALUES('%s', '%s')" % (username, password)
    #修改为你表里面的参数INSERT INTO {表名}({存放用户字段名}, {存放密码字段名})VALUES('%s', '%s')" % (username, password)
    query(sql)
    sql2 = "select * from user where name= '" + username + "' and password= '" + password + "'"
    #修改为你表里面的参数select * from {表名} where {存放用户字段名}= '" + username + "' and {存放密码字段名}= '" + password + "'"
    res = query(sql2)
    return res



if __name__ == "__main__":
    app.run(debug=True)

