## 安装依赖
pip install -r requirements/local.txt

## 配置数据库
修改 config/settings/base.py, 46 行
"default": env.db("DATABASE_URL", default="mysql://root:Alisa123.@127.0.0.1:3306/scenario")
修改对应的密码和数据库名即可
