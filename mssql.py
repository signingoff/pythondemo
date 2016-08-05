import pymssql

class SqlUtil:
    def __init__(self,server,userid,password,datatabase):
        self.server=server
        self.userid=userid
        self.password=password
        self.datatabase=datatabase

    def _get_connection(self):
        self.connection=pymssql.connect(host=self.server,user=self.userid,password=self.password,database=self.datatabase)
        cursor=self.connection.cursor()
        return cursor

    def execute_query(self,sql):
        cursor=self._get_connection()
        cursor.execute(sql)
        result=cursor.fetchall()
        self.connection.close()
        return result

    def execute_no_query(self,sql):
        cursor=self._get_connection()
        cursor.execute(sql)
        self.connection.commit()
        self.connection.close()

def main():
    util=SqlUtil("DAVID-PC\\MSSQLSERVER2008R","sa","1","AspNetCore")
    for (MigrationId,ProductVersion) in util.execute_query("select * from __EFMigrationsHistory"):
        print(MigrationId.rjust(45,' ')+"    "+ProductVersion)

    util.execute_no_query("Update __EFMigrationsHistory set ProductVersion='12'")

if __name__=="__main__":
    main()