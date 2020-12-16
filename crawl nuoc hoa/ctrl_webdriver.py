from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests


browser = webdriver.Chrome()
browser.minimize_window()

def check_ad():
	if browser.find_element_by_css_selector('div.card').is_display(): browser.find_element_by_css_selector('div#dismiss-button').click()
	elif browser.find_element_by_css_selector('div#ad_position_box').is_display(): browser.find_element_by_css_selector('div#dismiss-button').click()

def down_image(link, name):
	name_image = '_'.join(split(name))
	with open(f"D:\\python\\crawl nuoc hoa\\media\\{name_image}.jpg", "wb+") as f:
		image = requests.get(link).content
		f.write(image)
	return '..\\media\\' + name_image + '.jpg'

def nhom_mui():
	browser.get("https://perfumista.vn/mui-huong-nuoc-hoa")
	check_ad()
	# nhom_mui = []
	# for item in browser.find_elements_by_css_selector('ul.item-wrapper p'): nhom_mui.append(item.text)
	links = []
	for item in browser.find_elements_by_css_selector('ul.item-wrapper.grid-list.note-wrapper.note-group-wrapper.clearfix a'):
		links.append(item.get_attribute('href'))
	return links

def loai_mui(link):
	browser.get(link)
	check_ad()
	while browser.find_element_by_css_selector('button.load-more-item').is_displayed():
		browser.find_element_by_css_selector('button.load-more-item').click()
		check_ad()
	ten = browser.find_element_by_css_selector('h1.item-title').text
	mo_ta = browser.find_element_by_css_selector('div.page-description').text
	link_image = browser.find_element_by_css_selector('ul.page-cover img').get_attribute('src')
	link = down_image(link_image, ten)
	mui = []
	for item in browser.find_elements_by_css_selector('ul.item-wrapper.grid-list.note-group-detail-wrapper.clearfix p'):
		mui.append(item.text)
	return {
		'ten': ten,
		'mo_ta': mo_ta,
		'link': link,
		'mui': mui,
	}

def mui_huong(link):
	browser.get(link)
	check_ad()
	ten = browser.find_element_by_css_selector('h1.item-title').text
	links_image = browser.find_elements_by_css_selector('li.item img').get_attribute('src')
	links = []
	for link in links_image:
		i = 0
		links.append(down_image(link, ten + i))
		i += 1
	mo_ta = browser.find_element_by_css_selector('div.page-description').text
	return {
		'ten': ten,
		'links': links,
		'mo_ta': mo_ta
	}

def thuong_hieu():
	browser.get("https://perfumista.vn/thuong-hieu-nuoc-hoa")
	check_ad()
	links = []
	for item in browser.find_elements_by_css_selector('ul#content-view-square a'): links.append(item.get_attribute('href'))
	return links

def get_thuong_hieu(link):
	browser.get(link)
	check_ad()
	ten = browser.find_element_by_css_selector('h1.item-title').text[14:]
	quoc_gia = browser.find_element_by_css_selector('div.brand-intro a').text
	link_image = down_image(link, ten)
	return {
		'ten': ten,
		'quoc_gia': quoc_gia,
		'link_image':link_image
	}

def gets_sp():
	links = []
	for item in browser.find_elements_by_css_selector('li.post-item a'): links.append(item.get_attribute('href'))
	return links

def get_sp(link):
	browser.get(link)
	check_ad()
	info = browser.find_elements_by_css_selector('div.des-group p')
	nuoc_hoa = browser.find_element_by_css_selector('h3.title')
	nhom = info[0].text[15:]
	gioi_tinh = info[1].text[11:]
	tuoi = info[2].text[21:]
	nam_sx = info[3].text[12:]
	nong_do = info[4].text[9:]
	pha_che = info[5].text[13:]
	do_luu = info[6].text[14:]
	do_toa = info[7].text[14:]
	khuyen_dung = info[8].text[23:]
	phong_cach = info[9].text[12:]
	diem = browser.find_element_by_css_selector('div.col-xs-2 cl6.rating-point').text
	huong_dau = []
	huong_chinh = []
	huong_cuoi = []
	gia_tien = []
	if len(info) == 12:
		for huong in info[10].text[13:].split(','): huong_chinh.append(huong.strip())
	else:
		for huong in info[10].text[11:].split(','): huong_chinh.append(huong.strip())
		for huong in info[12].text[12:].split(','): huong_chinh.append(huong.strip())
		for huong in info[14].text[12:].split(','): huong_chinh.append(huong.strip())
	if browser.find_element_by_css_selector('ul.order-items.clearfix').is_displayed():
		if browser.find_element_by_css_selector('a.order-shop-item-readmore').is_displayed():
			browser.find_element_by_css_selector('a.order-shop-item-readmore').click()
			for line in browser.find_element_by_css_selector('ul.order-items.clearfix').text.split('\n'): gia_tien.append(line)
		else:
			for line in browser.find_element_by_css_selector('ul.order-items.clearfix').text.split('\n'): gia_tien.append(line)
	return {
		'nuoc_hoa': nuoc_hoa,
		'nhom': nhom,
		'gioi_tinh': gioi_tinh,
		'tuoi': tuoi,
		'nam_sx': nam_sx,
		'nong_do': nong_do,
		'pha_che': pha_che,
		'do_luu': do_luu,
		'do_toa': do_toa,
		'khuyen_dung': khuyen_dung,
		'phong_cach': phong_cach,
		'diem': diem,
		'huong_dau': huong_dau,
		'huong_chinh': huong_chinh,
		'huong_cuoi': huong_cuoi,
		'gia_tien': gia_tien,
	}
