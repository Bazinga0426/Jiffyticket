## install dependency 
pip install -r requirements/local.txt

## config database
Modify config/settings/base.py, 46 line
"default": env.db("DATABASE_URL", default="mysql://root:password.@127.0.0.1:3306/database_name")

