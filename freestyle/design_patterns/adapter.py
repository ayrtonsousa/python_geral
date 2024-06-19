from abc import ABCMeta, abstractmethod


class OracleAdaptee:

    def insert_oracle():
        print('insert db oracle')

    def update_oracle():
        print('update db oracle')

    def delete_oracle():
        print('delete db oracle')


class MySQLAdaptee:

    def insert_mysql():
        print('insert db mysql')

    def update_mysql():
        print('update db mysql')

    def delete_mysql():
        print('delete db mysql')


class Adapter(metaclass=ABCMeta):

    @abstractmethod
    def insert_db(self):
        ...

    @abstractmethod
    def update_db(self):
        ...

    @abstractmethod
    def delete_db(self):
        ...

class MySQLDBAdapter(Adapter):

    def __init__(self, db_mysql):
        self.mysql = db_mysql

    def insert_db(self):
        self.mysql.insert_mysql()

    def update_db(self):
        self.mysql.update_mysql()

    def delete_db(self):
        self.mysql.delete_mysql()

class OracleDBAdapter(Adapter):

    def __init__(self, db_oracle):
        self.oracle = db_oracle

    def insert_db(self):
        self.oracle.insert_oracle()

    def update_db(self):
        self.oracle.update_oracle()

    def delete_db(self):
        self.oracle.delete_oracle()

if __name__ == '__main__':
    oracle = OracleDBAdapter(OracleAdaptee)
    oracle.insert_db()
    oracle.update_db()
    oracle.delete_db()

    mysql = MySQLDBAdapter(MySQLAdaptee)
    mysql.insert_db()
    mysql.update_db()
    mysql.delete_db()