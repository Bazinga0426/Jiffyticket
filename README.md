<<<<<<< HEAD
## 安装依赖
pip install -r requirements/local.txt

=======
## install dependency 
pip install -r requirements/local.txt

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705
## 配置数据库
修改 config/settings/base.py, 46 行
"default": env.db("DATABASE_URL", default="mysql://root:Alisa123.@127.0.0.1:3306/scenario")
修改对应的密码和数据库名即可
<<<<<<< HEAD

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

# 样式参考
https://www.movietickets.com/movie/ford-v-ferrari/27b621dd-46c0-3deb-90be-d63e84f9fc32

# OWASP
https://xz.aliyun.com/t/4916

# 设计模式
strategy pattern(在下面的文件中搜索 strategy，我做了注释)
    - 通过策略模式完成折扣部分
    - bscenario/movies/views.py
    - bscenario/orders/views.py
    
state design pattern(搜索 #state)
    - 获取不同类型的票价
    - bscenario/movies/models.py

factory method pattern(搜索 #factory)
    - 打印不同的 ticket
    - bscenario/tickets/models.py 
    - bscenario/movies/views.py
=======
=======
## config database
Modify config/settings/base.py, 46 line
"default": env.db("DATABASE_URL", default="mysql://root:password.@127.0.0.1:3306/database_name")

>>>>>>> bb94a30e6054f442315fba7fd8854fd9a3f433bb
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705
>>>>>>> 6a246fab5a70703ca261e8ccae458db63a17ccde
