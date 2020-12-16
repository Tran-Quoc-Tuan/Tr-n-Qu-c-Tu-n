import ctrl_db
import ctrl_webdriver


db = ctrl_db.connect()
cur = ctrl_db.cursor(db)
ctrl_db.create_table(cur)


ctrl_db.commit(cur)
ctrl_db.close_db(db)
cur.commit()
db.close()
