
class EngineBase:
    """enginebase 只定义了init函数和若干方法的名字, 具体实现用mysql.py pg.py等实现"""

    def __init__(self, instance=None):
        self.conn = None
        if instance:
            self.instance = instance
            self.instance_name = instance.instance_name
            self.host = instance.host
            self.port = int(instance.port)
            self.user = instance.user
            self.password = instance.raw_password

def get_engine(instance=None):

    """获取数据库操作engine"""
    if instance.db_type == 'MySQL':
        from .mysql import MySQLEngine
        return MySQLEngine(instance=instance)
    elif instance.db_type == 'mssql':
        from .mssql import MssqlEngine
        return MssqlEngine(instance=instance)
    elif instance.db_type == 'redis':
        from .redis import RedisEngine
        return RedisEngine(instance=instance)
    elif instance.db_type == 'pgsql':
        from .pgsql import PgSQLEngine
        return PgSQLEngine(instance=instance)
    elif instance.db_type == 'oracle':
        from .oracle import OracleEngine
        return OracleEngine(instance=instance)
    elif instance.db_type == 'inception':
        from .inception import InceptionEngine
        return InceptionEngine(instance=instance)
    elif instance.db_type == 'goinception':
        from .goinception import GoInceptionEngine
        return GoInceptionEngine(instance=instance)