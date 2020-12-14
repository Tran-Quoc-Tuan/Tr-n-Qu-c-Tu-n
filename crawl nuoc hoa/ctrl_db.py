import sqlite3


def connect():
	return sqlite3.connect("database.sqlite3")

def cursor(database_name):
	return database_name.cursor()

def create_table(cursor):
	cur.execute('''
		CREATE TABLE IF NOT EXISTS NHOM_HUONG(
			ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Ten_nhom TEXT --Tên các nhóm hương
		)

		CREATE TABLE IF NOT EXISTS MUI_HUONG(
			ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Ten_huong TEXT, --Tên mùi hương
			Nhom_mui TEXT,  --Thuộc nhóm mùi
			FOREIGN KEY(Nhom_mui) REFERENCES NHOM_HUONG(Ten_nhom)
		)

		CREATE TABLE IF NOT EXISTS NHA_PHA_CHE (
			ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Ten TEXT --Tên nhà pha chế
		)

		CREATE TABLE IF NOT EXISTS THUONG_HIEU(
			ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Ten_hang TEXT NOT NULL, --Tên hãng
			Quoc_gia TEXT,          --Quốc gia
			Link TEXT,              --Link ảnh
		)

		CREATE TABLE IF NOT EXISTS NUOC_HOA(
			ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Nuoc_hoa TEXT NOT NULL, --Tên nước hoa
			Hang_sx TEXT,           --Hãng sản xuất
			Nhom TEXT,              --Thuộc nhóm nước hoa
			Gioi_tinh TEXT,         --Dành cho nam/nữ/unisex
			Tuoi TEXT,              --Tuổi phù hợp
			Nam_sx TEXT,            --Năm sản xuất
			Nong_do TEXT,           --Nồng độ
			Pha_che TEXT,           --Nhà pha chế
			Do_luu TEXT,            --Độ lưu hương
			Do_toa TEXT,            --Độ tỏa hương
			Kuyen_dung TEXT,        --Thời điểm khuyên dùng
			Phong_cach TEXT,        --Phong cách phù hợp
			Huong_dau TEXT,         --Hương đầu
			Huong_chinh TEXT,       --Hương chính
			Huong_cuoi TEXT,        --Hương cuối
			Diem REAL,              --Điểm đánh giá
			Tong_quan TEXT,         --Đánh giá tổng quan
			Link TEXT,              --Link ảnh sản phẩm
			FOREIGN KEY(Pha_che) REFERENCES NHA_PHA_CHE(Ten)
			FOREIGN KEY(Hang_sx) REFERENCES THUONG_HIEU(Ten_hang)
			FOREIGN KEY(Huong_dau) REFERENCES MUI_HUONG(Ten_huong)
			FOREIGN KEY(Huong_cuoi) REFERENCES MUI_HUONG(Ten_huong)
			FOREIGN KEY(Huong_chinh) REFERENCES MUI_HUONG(Ten_huong)
		)

		CREATE TABLE IF NOT EXISTS GIA_TIEN(
			Nuoc_hoa TEXT NOT NULL, --Tên nước hoa
			Loai TEXT,              --Loại sản phẩm
			Gia REAL,               --Giá thành
			FOREIGN KEY(Nuoc_hoa) REFERENCES NUOC_HOA(Nuoc_hoa)
		)

		CREATE TABLE IF NOT EXISTS BLOG(
			ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			Title TEXT,     --Tiêu đề blog
			Date_cre DATE,  --Ngày tạo blog
			Content TEXT	--Nội dung blog
		)
	''')

def commit(cursor):
	return cursor.commit()

def close_db(database_name):
	return database_name.close()

if __name__ == __main__:
	pass
