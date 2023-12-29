# Flask-ML-Project
 
------
## 简介
大学生python实训的答辩项目，项目较为简单，适用于新手入门python，flask。
## 项目说明
 本项目为共享单车需求预测网站，项目通过机器学习训练好的共享单车数据集构建的模型，在前端网页中输入预估的参数，由flask后端调用，再返回出结果。
> * 前端（html+css+js）
> * 后端（Flask）
> * 数据库（MySQL）
> * 模型保存、训练（sklearn）
<br>
输入/admin 进入后台（功能未完善，仅展示）


### 一. 如何使用
1.pip安装**requirements.txt**中的python库，不用特别限制库的版本，安最新的即可
>* [pip安装教程](https://blog.csdn.net/aobulaien001/article/details/133298563)

2.安装**MySQL**数据库，并新建好数据库，添加好表等信息<br>
（不想修改代码的话，数据库应直接添加，账号：root、密码：root、库名：db1、表：user，字段：name和password）
<br>
>* [mysql数据库安装教程](https://blog.csdn.net/a802976/article/details/119255644
)
>* [mysql数据库配置教程](https://blog.csdn.net/weixin_45851945/article/details/114287877)<br>
### 二.数据库安装好后，想偷懒可以直接复制我的命令配置
<br>
打开cmd
<br>
<pre><code>
net start mysql  #启动MySQL


mysql -uroot -p  #连接 输入完后回车，会让你输入你的密码


ALTER USER 'root'@'localhost' IDENTIFIED BY 'root'; #修改密码为root


create database db1; #新建数据库'db1'


use db1; #打开数据库'db1'


create table user(name varchar(10),password varchar(20)); #创建用户‘user’表 

 
show create table user;  #查看效果，有即添加成功


</code></pre>
### 三.运行
<pre><code>
python app.py
 #或者打开编译器，直接运行app.py文件
 #浏览器输入172.0.0.1:5000进入网站
</code></pre>

## 项目贡献/参考


前端代码贡献[@PCDL233](https://github.com/PCDL233)<br>
模型训练部分[@hczs](https://github.com/hczs/data-mining)

## [项目效果展示]()
