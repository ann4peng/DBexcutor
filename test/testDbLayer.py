import sqlite3

from RockModels import MeterData
from SqlExecutor import SqlExecutor

cx = sqlite3.connect("C:\Ann\LiAn\DBLayer\db.sqlite3")
cu = cx.cursor()
sqlexecutor = SqlExecutor(cx)
sqlexecutor.convertSql = False
# Insert a new line of data into a table by creating a new object and give data "Ohohoohxxxx"
sqlexecutor.insert(MeterData("Ohohoohxxxx"), "meter_data")

print sqlexecutor.execRawSqlFetchOne("select * from meter_data where id = ?", (4560))
print sqlexecutor.execRawSqlFetchAll("select * from meter_data where id = ?", (4561))
print sqlexecutor.execSqlSingle("select * from meter_data where id = ?", [4560], MeterData)
print sqlexecutor.execSqlAll("select * from meter_data ", [], MeterData)

