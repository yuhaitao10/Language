import pytest
from mydb import MyDB
from mydb import Connection
from mydb import Cursor

@pytest.fixture(scope="module")
def cur():
  print("Setting up")
  db = MyDB()
  conn = db.connection("server")
  curs = conn.cursor()
  yield curs
  curs.close()
  conn.close()
  print("closing DB")
  return curs


def test_john_id(cur):
    #db = MyDB()
    #conn = db.connect("server")
    #cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=John")
    assert id  == 123


def test_toms_id(cur):
    #db = MyDB()
    #conn = db.connect("server")
    #cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=Tom")
    assert id  == 789
