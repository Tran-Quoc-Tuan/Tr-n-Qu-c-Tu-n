import sqlite3


def connect():
	return sqlite3.connect("database.sqlite3")


def cursor(database_name):
	return database_name.cursor()


def get_data(query):
	try: return query.fetchall()[0][0]
	except IndexError: return ''


def create_table(cursor):
	cursor.executescript('''
		CREATE TABLE IF NOT EXISTS IMAGE(
			ID   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			Link TEXT
		);

		CREATE TABLE IF NOT EXISTS NHOM_HUONG(
			Ten_nhom TEXT PRIMARY KEY, --Tên các nhóm hương
			Mo_ta    TEXT,
			Link     TEXT
		);

		CREATE TABLE IF NOT EXISTS MUI_HUONG(
			'id'       integer NOT NULL PRIMARY KEY AUTOINCREMENT,
			Ten_huong  TEXT, --Tên mùi hương
			Nhom_mui   TEXT, --Thuộc nhóm mùi
			Mo_ta      TEXT, --Mô tả về mùi hương
			--Link_image table ANH_MUI_HUONG    --Link ảnh
			FOREIGN KEY(Nhom_mui)   REFERENCES NHOM_HUONG(Ten_nhom)
		);

		CREATE TABLE IF NOT EXISTS ANH_MUI_HUONG(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			Mui_huong_id  INTEGER NOT NULL,
			Image_id      INTEGER NOT NULL,
			FOREIGN KEY(Mui_huong_id) REFERENCES MUI_HUONG(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(Image_id)     REFERENCES IMAGE(ID) DEFERRABLE INITIALLY DEFERRED
		);

		CREATE TABLE IF NOT EXISTS NHA_PHA_CHE(
			Ten        TEXT PRIMARY KEY, --Tên nhà pha chế
			Gioi_thieu TEXT,             --Bài giới thiệu
			Link_image TEXT              --Link ảnh
		);

		CREATE TABLE IF NOT EXISTS THUONG_HIEU(
			ID         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Ten_hang   TEXT NOT NULL,     --Tên hãng
			Quoc_gia   TEXT,              --Quốc gia
			Gioi_thieu TEXT,              --bài viết giới thiệu về thương hiệu
			Link_web   TEXT,              --Link trang chủ
			Link_image TEXT               --Link ảnh
		);

		CREATE TABLE IF NOT EXISTS NUOC_HOA(
			ID          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Nuoc_hoa    TEXT NOT NULL, --Tên nước hoa
			Hang_sx     INTEGER,       --Hãng sản xuất
			Nhom        TEXT,          --Thuộc nhóm nước hoa
			Gioi_tinh   TEXT,          --Dành cho nam/nữ/unisex
			Tuoi        TEXT,          --Tuổi phù hợp
			Nam_sx      TEXT,          --Năm sản xuất
			Nong_do     TEXT,          --Nồng độ
			Pha_che     TEXT,          --Nhà pha chế
			Do_luu      TEXT,          --Độ lưu hương
			Do_toa      TEXT,          --Độ tỏa hương
			Khuyen_dung TEXT,          --Thời điểm khuyên dùng
			Phong_cach  TEXT,          --Phong cách phù hợp
			Diem        REAL,          --Điểm đánh giá
			Tong_quan   TEXT,          --Đánh giá tổng quan(html)
			Chi_tiet    TEXT,          --Đánh giá chi tiết(html)
			--Huong_dau   table HUONG_DAU         --Hương đầu
			--Huong_chinh table HUONG_CHINH       --Hương chính
			--Huong_cuoi  table HUONG_CUOI        --Hương cuối
			--Link_image  table ANH_NUOC_HOA      --Link ảnh sản phẩm
			FOREIGN KEY(Pha_che) REFERENCES NHA_PHA_CHE(Ten),
			FOREIGN KEY(Hang_sx) REFERENCES THUONG_HIEU(ID)
		);

		CREATE TABLE IF NOT EXISTS ANH_NUOC_HOA(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			Nuoc_hoa_id   INTEGER NOT NULL,
			Image_id      INTEGER NOT NULL,
			FOREIGN KEY(Nuoc_hoa_id) REFERENCES NUOC_HOA(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(Image_id)    REFERENCES IMAGE(ID) DEFERRABLE INITIALLY DEFERRED
		);

		CREATE TABLE IF NOT EXISTS HUONG_DAU(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			Nuoc_hoa_id   INTEGER NOT NULL,
			Mui_huong_id  INTEGER NOT NULL,
			FOREIGN KEY(Nuoc_hoa_id)  REFERENCES NUOC_HOA(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(Mui_huong_id) REFERENCES MUI_HUONG(ID) DEFERRABLE INITIALLY DEFERRED
		);

		CREATE TABLE IF NOT EXISTS HUONG_CHINH(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			Nuoc_hoa_id   INTEGER NOT NULL,
			Mui_huong_id  INTEGER NOT NULL,
			FOREIGN KEY(Nuoc_hoa_id)  REFERENCES NUOC_HOA(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(Mui_huong_id) REFERENCES MUI_HUONG(ID) DEFERRABLE INITIALLY DEFERRED
		);

		CREATE TABLE IF NOT EXISTS HUONG_CUOI(
			ID	          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			Nuoc_hoa_id   INTEGER NOT NULL,
			Mui_huong_id  INTEGER NOT NULL,
			FOREIGN KEY(Nuoc_hoa_id)  REFERENCES NUOC_HOA(ID) DEFERRABLE INITIALLY DEFERRED,
			FOREIGN KEY(Mui_huong_id) REFERENCES MUI_HUONG(ID) DEFERRABLE INITIALLY DEFERRED
		);

		CREATE TABLE IF NOT EXISTS GIA_TIEN(
			Nuoc_hoa_id INTEGER NOT NULL, --Tên nước hoa
			Noi_ban     TEXT,          --Loại sản phẩm và website bán
			Gia         REAL,          --Giá thành
			FOREIGN KEY(Nuoc_hoa_id) REFERENCES NUOC_HOA(ID)
		);

		CREATE TABLE IF NOT EXISTS BLOG(
			ID       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Title    TEXT, --Tiêu đề blog
			Date_cre TEXT, --Ngày tạo blog
			Content  TEXT  --Nội dung blog
		);
	''')


def insert_image(cursor, Link):
	value = (Link, )
	cursor.execute("INSERT INTO IMAGE (Link) VALUES(?)", value)


def select_image(cursor, Link):
	value = (Link, )
	data = cursor.execute("SELECT ID FROM IMAGE WHERE Link = ?", value)
	return get_data(data)


def insert_anh_huong(cursor, id_image, id_mui_huong):
	value = (id_image, id_mui_huong)
	cursor.execute("INSERT INTO ANH_MUI_HUONG (Mui_huong_id, Image_id) VALUES(?, ?)", value)


def insert_anh_nuoc_hoa(cursor, id_nuoc_hoa, id_image):
	value = (id_nuoc_hoa, id_image)
	cursor.execute("INSERT INTO ANH_NUOC_HOA (Nuoc_hoa_id, Image_id) VALUES(?, ?)", value)


def insert_nhom_huong(cursor, Ten_nhom, Mo_ta, Link):
	value = (Ten_nhom, Mo_ta, Link)
	cursor.execute("INSERT INTO NHOM_HUONG VALUES(?, ?, ?)", value)


def select_nhom_huong(cursor, Ten_nhom):
	value = (Ten_nhom, )
	data = cursor.execute("SELECT ID FROM NHOM_HUONG WHERE Ten_nhom = ?", value)
	return get_data(data)


def insert_mui_huong(cursor, Ten_huong, Nhom_mui, Mo_ta):
	value = (Ten_huong, Nhom_mui, Mo_ta)
	cursor.execute("INSERT INTO MUI_HUONG (Ten_huong, Nhom_mui, Mo_ta) VALUES(?, ?, ?)", value)


def select_mui_huong(cursor, Ten_huong):
	value = (Ten_huong, )
	data = cursor.execute("SELECT ID FROM MUI_HUONG WHERE Ten_huong = ?", value)
	return get_data(data)


def insert_nha_pha_che(cursor, Ten, Gioi_thieu, Link_image):
	value = (Ten, Gioi_thieu, Link_image)
	cursor.execute("INSERT INTO NHA_PHA_CHE (Gioi_thieu, Link_image) VALUES(?, ?, ?)", value)


def select_nha_pha_che(cursor, Ten):
	value = (Ten, )
	data = cursor.execute("SELECT Ten FROM NHA_PHA_CHE WHERE Ten = ?", value)
	return get_data(data)


def insert_thuong_hieu(cursor, Ten_hang, Quoc_gia, Link_web, Link_image):
	value = (Ten_hang, Quoc_gia, Link_web, Link_image)
	cursor.execute("INSERT INTO THUONG_HIEU (Ten_hang, Quoc_gia, Gioi_thieu, Link_web, Link_image) VALUES(?, ?, ?, ?)", value)


def select_thuong_hieu(cursor, Ten_hang):
	value = (Ten_hang, )
	data = cursor.execute("SELECT ID FROM THUONG_HIEU WHERE Ten_hang = ?", value)
	return get_data(data)


def insert_nuoc_hoa(cursor, Nuoc_hoa, Hang_sx_id, Nhom, Gioi_tinh, Tuoi, Nam_sx, Nong_do, Pha_che, Do_luu, Do_toa, Khuyen_dung, Phong_cach, Diem, Tong_quan, Chi_tiet):
	value = (Nuoc_hoa, Hang_sx_id, Nhom, Gioi_tinh, Tuoi, Nam_sx, Nong_do, Pha_che, Do_luu, Do_toa, Khuyen_dung, Phong_cach, Diem, Tong_quan, Chi_tiet)
	cursor.execute("INSERT INTO NUOC_HOA (Nuoc_hoa, Hang_sx, Nhom, Gioi_tinh, Tuoi, Nam_sx, Nong_do, Pha_che, Do_luu, Do_toa, Khuyen_dung, Phong_cach, Diem, Tong_quan, Chi_tiet) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", value)


def select_nuoc_hoa(cursor, Nuoc_hoa):
	value = (Nuoc_hoa, )
	data = cursor.execute("SELECT ID FROM NUOC_HOA WHERE Nuoc_hoa = ?", value)
	return get_data(data)


def insert_huong_dau(cursor, id_nuoc_hoa, id_mui_huong):
	value = (id_nuoc_hoa, id_mui_huong)
	cursor.execute("INSERT INTO HUONG_DAU (Nuoc_hoa_id, Mui_huong_id) VALUES(?, ?)", value)


def insert_huong_chinh(cursor, id_nuoc_hoa, id_mui_huong):
	value = (id_nuoc_hoa, id_mui_huong)
	cursor.execute("INSERT INTO HUONG_CHINH (Nuoc_hoa_id, Mui_huong_id) VALUES(?, ?)", value)


def insert_huong_cuoi(cursor, id_nuoc_hoa, id_mui_huong):
	value = (id_nuoc_hoa, id_mui_huong)
	cursor.execute("INSERT INTO HUONG_CUOI (Nuoc_hoa_id, Mui_huong_id) VALUES(?, ?)", value)


def insert_gia_tien(cursor, Nuoc_hoa_id, Noi_ban, Gia):
	value = (Nuoc_hoa_id, Noi_ban, Gia)
	cursor.execute("INSERT INTO GIA_TIEN VALUES(?, ?, ?)", value)


def insert_blog(cursor, Title, Date_cre, Content):
	value = (Title, Date_cre, Content)
	cursor.execute("INSERT INTO BLOG (Title, Date_cre, Content) VALUES(?, ?, ?)", value)


def commit(database_name):
	database_name.commit()


def close_db(database_name):
	database_name.close()


if __name__ == '__main__':
	db = connect()
	cursor = cursor(db)
	create_table(cursor)
	commit(db)
	close_db(db)
