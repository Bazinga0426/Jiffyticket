## 安装依赖
pip install -r requirements/local.txt

## 配置数据库
修改 config/settings/base.py, 46 行
"default": env.db("DATABASE_URL", default="mysql://root:Alisa123.@127.0.0.1:3306/scenario")
修改对应的密码和数据库名即可

## 运行命令
创建数据库表: python manage.py migrate
python manage.py runserver


#网页说明
/: 主要，显示电影列表
/detail/1/: 电影详情
右上角是用户注册登录

# 管理员
生成管理员帐号: python manage.py createsuperuser, 根据提示创建管理员帐号
http://127.0.0.1:8000/admin/, 进入此页面能看到各个对象的管理，比如用户的增删改查，电影的增删改查


# 策略模式
折扣那部分
