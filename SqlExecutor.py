from LeeUtil import LeeUtil

__author__ = 'Ann'


class SqlExecutor:
    convertSql = not False

    def __init__(self, con):
        self.connection = con
        self.lambdaFetchOne = lambda x: x.fetchone()
        self.lambdaFetchAll = lambda x: x.fetchall()

    def execSqlAll(self, sql, args, clz=None):
        cursor = self.getCursor()  # cursor must be in the same method stack
        return self.__sqlResult2object(self.__execRawSqlUsingCursor(cursor, self.lambdaFetchAll, sql, *args), clz,
                                       cursor)

    def execSqlSingle(self, sql, args, clz=None):
        cursor = self.getCursor()
        return self.__sqlResult2object(self.__execRawSqlUsingCursor(cursor, self.lambdaFetchOne, sql, *args), clz,
                                       cursor)

    def execRawSqlFetchAll(self, sql, *args):
        return self.__execRawSqlUsingCursor(self.getCursor(), self.lambdaFetchAll, sql, *args)

    def execRawSqlFetchOne(self, sql, *args):
        return self.__execRawSqlUsingCursor(self.getCursor(), self.lambdaFetchOne, sql, *args)

    # remove the table ID when insert new data to avoid duplicate issue
    def insert(self, entity, table, tableId=None):
        ins = self.__buildInsert(entity, table, tableId)
        self.connection.execute(self.__processSql(ins[0]), ins[1])
        self.connection.commit()

    def getCursor(self):
        return self.connection.cursor()

    def __execRawSqlUsingCursor(self, cursor, lambdaCursor, sql, *args):
        if not args:
            args = ()
        sql = self.__processSql(sql)
        cursor.execute(sql, args)
        re = lambdaCursor(cursor)
        cursor.close()
        return re
    # if connect database via django , '?' is not supported, but if connect the database via import sqlite3, this function is not needed
    def __processSql(self, sql):
        return sql.replace('?', '%s') if self.convertSql else sql

    def __buildInsert(self, a, table, tableId=None):
        fs = LeeUtil.getFields(a)
        if tableId:
            fs.remove(tableId)
        args = [getattr(a, f) for f in fs]
        # fsInInsert = ",".join(["'" + attr + "'" for attr in fs])
        fsInInsert = ",".join([attr for attr in fs])
        placeHolders = LeeUtil.genPlaceHolders(len(fs))
        insert = '''insert into {0}({1}) values({2})'''.format(table, fsInInsert, placeHolders)
        return insert, args

    def __sqlResult2object(self, sqlResult, clz, cu):
        if isinstance(sqlResult, list):
            res = []
            for i in sqlResult:
                res.append(self.__sqlResult2object(i, clz, cu))
            return res
        if not clz:
            return sqlResult
        res = clz()
        fs = [tuple[0] for tuple in cu.description]
        print len(sqlResult)
        print len(fs)
        for i in range(0,  len(fs)):
            setattr(res, fs[i], sqlResult[i])
        return res
