import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 两种方式：
    # 1. 使用环境变量 （like deploy）
    # 2. 使用SQLite数据库 （like develop）
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
