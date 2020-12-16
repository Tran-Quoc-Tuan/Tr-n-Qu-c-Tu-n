import sqlite3


def connect():
	return sqlite3.connect("database.sqlite3")


def cursor(database_name):
	return database_name.cursor()


def create_table(cur):
	cur.execute('''
		CREATE TABLE IF NOT EXISTS IMAGE(
			ID   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			Name TEXT,
			Link TEXT
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS NHOM_HUONG(
			Ten_nhom TEXT PRIMARY KEY, --Tên các nhóm hương
			Mo_ta    TEXT,
			Link     TEXT
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS MUI_HUONG(
			ID	       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			Ten_huong  TEXT, --Tên mùi hương
			Nhom_mui   TEXT,             --Thuộc nhóm mùi
			Mo_ta      TEXT,			 --Mô tả về mùi hương
			--Link_image table ANH_MUI_HUONG    --Link ảnh
			FOREIGN KEY(Nhom_mui)   REFERENCES NHOM_HUONG(Ten_nhom)
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS ANH_MUI_HUONG(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			mui_huong_id  INTEGER NOT NULL,
			image_id      INTEGER NOT NULL,
			FOREIGN KEY(mui_huong_id) REFERENCES MUI_HUONG(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(image_id)     REFERENCES IMAGE(ID) DEFERRABLE INITIALLY DEFERRED
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS NHA_PHA_CHE (
			ID         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Ten        TEXT, --Tên nhà pha chế
			Gioi_thieu TEXT, --Bài giới thiệu
			Link_image TEXT --Link ảnh
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS THUONG_HIEU(
			ID         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Ten_hang   TEXT NOT NULL,     --Tên hãng
			Quoc_gia   TEXT,              --Quốc gia
			Gioi_thieu TEXT,              --bài viết giới thiệu về thương hiệu
			Link_web   TEXT,              --Link trang chủ
			Link_image TEXT              --Link ảnh
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS NUOC_HOA(
			ID          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Nuoc_hoa    TEXT NOT NULL, --Tên nước hoa
			Hang_sx     TEXT,          --Hãng sản xuất
			Nhom        TEXT,          --Thuộc nhóm nước hoa
			Gioi_tinh   TEXT,          --Dành cho nam/nữ/unisex
			Tuoi        TEXT,          --Tuổi phù hợp
			Nam_sx      TEXT,          --Năm sản xuất
			Nong_do     TEXT,          --Nồng độ
			Pha_che     TEXT,          --Nhà pha chế
			Do_luu      TEXT,          --Độ lưu hương
			Do_toa      TEXT,          --Độ tỏa hương
			Kuyen_dung  TEXT,          --Thời điểm khuyên dùng
			Phong_cach  TEXT,          --Phong cách phù hợp
			Diem        REAL,          --Điểm đánh giá
			Tong_quan   TEXT,          --Đánh giá tổng quan
			Chi_tiet    TEXT,          --Đánh giá chi tiết
			--Huong_dau   table HUONG_DAU         --Hương đầu
			--Huong_chinh table HUONG_CHINH       --Hương chính
			--Huong_cuoi  table HUONG_CUOI        --Hương cuối
			--Link_image  table ANH_NUOC_HOA      --Link ảnh sản phẩm
			FOREIGN KEY(Pha_che)     REFERENCES NHA_PHA_CHE(Ten) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(Hang_sx)     REFERENCES THUONG_HIEU(Ten_hang)
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS ANH_NUOC_HOA(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			nuoc_hoa_id   INTEGER NOT NULL,
			image_id      INTEGER NOT NULL,
			FOREIGN KEY(nuoc_hoa_id)  REFERENCES NUOC_HOA(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(image_id)     REFERENCES IMAGE(ID) DEFERRABLE INITIALLY DEFERRED
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS HUONG_DAU(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			nuoc_hoa_id   INTEGER NOT NULL,
			mui_huong_id  INTEGER NOT NULL,
			FOREIGN KEY(nuoc_hoa_id)  REFERENCES NUOC_HOA(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(mui_huong_id) REFERENCES MUI_HUONG(ID) DEFERRABLE INITIALLY DEFERRED
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS HUONG_CHINH(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			nuoc_hoa_id   INTEGER NOT NULL,
			mui_huong_id  INTEGER NOT NULL,
			FOREIGN KEY(nuoc_hoa_id)  REFERENCES NUOC_HOA(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(mui_huong_id) REFERENCES MUI_HUONG(ID) DEFERRABLE INITIALLY DEFERRED
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS HUONG_CUOI(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			nuoc_hoa_id   INTEGER NOT NULL,
			mui_huong_id  INTEGER NOT NULL,
			FOREIGN KEY(nuoc_hoa_id)  REFERENCES NUOC_HOA(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(mui_huong_id) REFERENCES MUI_HUONG(ID) DEFERRABLE INITIALLY DEFERRED
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS GIA_TIEN(
			Nuoc_hoa TEXT NOT NULL, --Tên nước hoa
			Loai     TEXT,          --Loại sản phẩm
			Gia      REAL,          --Giá thành
			FOREIGN KEY(Nuoc_hoa) REFERENCES NUOC_HOA(Nuoc_hoa)
		)
	''')

	cur.execute('''
		CREATE TABLE IF NOT EXISTS BLOG(
			ID       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Title    TEXT, --Tiêu đề blog
			Date_cre DATE, --Ngày tạo blog
			Content  TEXT --Nội dung blog
		)
	''')


def commit(database_name):
	database_name.commit()


def close_db(database_name):
	database_name.close()


if __name__ == '__main__':
	db = connect()
	cur = cursor(db)
	create_table(cur)
	commit(db)
	close_db(db)
