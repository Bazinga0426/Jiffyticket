## install dependency 
pip install -r requirements/local.txt

<<<<<<< HEAD
## 配置数据库
修改 config/settings/base.py, 46 行
"default": env.db("DATABASE_URL", default="mysql://root:Alisa123.@127.0.0.1:3306/scenario")
修改对应的密码和数据库名即可
=======
## config database
Modify config/settings/base.py, 46 line
"default": env.db("DATABASE_URL", default="mysql://root:password.@127.0.0.1:3306/database_name")

>>>>>>> bb94a30e6054f442315fba7fd8854fd9a3f433bb
