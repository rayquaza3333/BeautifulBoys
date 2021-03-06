def replace(a, value_dict):
    with open(a, "r", encoding='utf-8') as f:
        text= f.read()

    for link in value_dict.keys():
        if link in text:
            text = text.replace(link,value_dict[link])

    with open(a, "w", encoding='utf-8') as f:
        f.write(text)
        f.close()




my_dict = {'https://angia.com.vn/vi/tin-tuc/cung-duong-resort-5-sao---con-at-chu-bai-giup-du-lich-vung-tau-thay-da-doi-thit.html':'142141',
'https://angia.com.vn/vi/tin-tuc/cung-duong-resort-5-sao---con-at-chu-bai-giup-du-lich-vung-tau-thay-da-doi-thit.html':'142142',
'https://angia.com.vn/vi/tin-tuc/cung-duong-resort-5-sao---con-at-chu-bai-giup-du-lich-vung-tau-thay-da-doi-thit.html':'142143',
'https://angia.com.vn/vi/tin-tuc/cung-duong-resort-5-sao---con-at-chu-bai-giup-du-lich-vung-tau-thay-da-doi-thit.html':'142144',
'https://angia.com.vn/vi/tin-tuc/cung-duong-resort-5-sao---con-at-chu-bai-giup-du-lich-vung-tau-thay-da-doi-thit.html':'142145',
'https://angia.com.vn/pictures/catalog/project-details/river-panorama/ho-boi-thuong-dinh-ven-song-tien-ich-4.jpg':'142146',
'https://angia.com.vn/vi/tin-tuc/dieu-chinh-quy-hoach-chung---buoc-ngoat-giup-vung-tau-lot-xac.html':'142147',
'https://angia.com.vn/vi/tin-tuc/5-loi-the-giup-vung-tau-but-pha-ngoan-muc-trong-nhung-nam-toi.html':'142148',
'https://angia.com.vn/vi/tin-tuc/trien-vong-lon-cho-thi-truong-can-ho-du-lich-vung-tau.html':'142149',
'https://angia.com.vn/vi/tin-tuc/khan-hiem-khach-san-can-ho-du-lich-5-sao-o-vung-tau.html':'142150',
'https://angia.com.vn/vi/tin-tuc/thong-bao-thoi-gian-lam-viec-tu-0208---05082019-1.html':'142151',
'https://angia.com.vn/pictures/catalog/news/tin-doanh-nghiep/THONGBAOTHUMB-500x325.jpg':'142152',
'https://angia.com.vn/vi/tin-tuc/bat-dong-san-vung-tau-don-nhan-don-bay-ha-tang.html':'142153',
'https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700|Google+Sans':'142154',
'https://angia.com.vn/pictures/catalog/news/tin-du-an/thesong/vungtau19.jpg':'142155',
'https://angia.com.vn/pictures/catalog/news/tin-du-an/thesong/vungtau17.jpg':'142156',
'https://angia.com.vn/pictures/catalog/news/tin-du-an/thesong/vungtau13.jpg':'142157',
'https://angia.com.vn/pictures/catalog/news/tin-du-an/thesong/vungtau12.jpg':'142158',
'https://angia.com.vn/pictures/catalog/news/tin-du-an/thesong/vungtau7.jpg':'142159',
'https://angia.com.vn/pictures/catalog/news/tin-du-an/thesong/vungtau6.jpg':'142160',
'https://angia.com.vn/catalog/view/theme/default/images/social-share.png':'142161',
'https://angia.com.vn/catalog/view/theme/default/images/social-share.png':'142162',
'https://angia.com.vn/catalog/view/theme/default/images/social-share.png':'142163',
'https://angia.com.vn/catalog/view/theme/default/images/favicon.png':'142164',
'https://angia.com.vn/catalog/view/theme/default/css/animation.css':'142165',
'https://angia.com.vn/catalog/view/theme/default/css/desktop.css':'142166',
'https://angia.com.vn/catalog/view/theme/default/css/header.css':'142167',
'https://angia.com.vn/catalog/view/theme/default/js/validate.js':'142168',
'https://angia.com.vn/catalog/view/theme/default/css/style.css':'142169',
'https://angia.com.vn/catalog/view/theme/default/css/slide.css':'142170',
'https://angia.com.vn/catalog/view/theme/default/js/animate.js':'142171',
'https://angia.com.vn/catalog/view/theme/default/js/jquery.js':'142172',
'https://angia.com.vn/catalog/view/theme/default/js/common.js':'142173',
'https://angia.com.vn/catalog/view/theme/default/js/scroll.js':'142174',
'https://angia.com.vn/catalog/view/theme/default/js/slide.js':'142175',
'http://online.gov.vn/CustomWebsiteDisplay.aspx?DocId=13027':'142176',
'https://angia.com.vn/catalog/view/theme/default/js/load.js':'142177',
'https://www.googletagmanager.com/gtag/js?id=UA-69962581-1':'142178',
'https://angia.com.vn/catalog/view/theme/default/js/btq.js':'142179',
'https://www.googletagmanager.com/ns.html?id=GTM-MPQ7V5L':'142180',
'https://angia.com.vn/pictures/catalog/logo-bct.png':'142181',
'https://angia.com.vn/vi/dich-vu-khach-hang-2.html':'142182',
'https://angia.com.vn/index.php?route=common/home':'142183',
'https://www.googletagmanager.com/gtm.js?id=':'142184',
'https://www.facebook.com/angia.investment':'142185',
'https://www.facebook.com/angia.investment':'142186',
'https://angia.com.vn/vi/nghe-nghiep.html':'142187',
'https://angia.com.vn/catalog/view/theme/':'142188',
'https://angia.com.vn/vi/gioi-thieu.html':'142189',
'https://angia.com.vn/vi/gioi-thieu.html':'142190',
'https://angia.com.vn/vi/gioi-thieu.html':'142191',
'https://angia.com.vn/en/news/-66.html':'142192',
'https://angia.com.vn/en/news/-66.html':'142193',
'https://angia.com.vn/vi/thu-vien.html':'142194',
'https://angia.com.vn/vi/thu-vien.html':'142195',
'https://angia.com.vn/vi/thu-vien.html':'142196',
'https://angia.com.vn/vi/tin-tuc.html':'142197',
'https://angia.com.vn/vi/lien-he.html':'142198',
'https://angia.com.vn/vi/tin-tuc.html':'142199',
'https://angia.com.vn/vi/lien-he.html':'142200',
'https://angia.com.vn/vi/tin-tuc.html':'142201',
'https://angia.com.vn/vi/tin-tuc.html':'142202',
'https://angia.com.vn/vi/lien-he.html':'142203',
'https://angia.com.vn/tim-kiem.html':'142204',
'https://angia.com.vn/tim-kiem.html':'142205',
'https://angia.com.vn/vi/du-an.html':'142206',
'https://angia.com.vn/vi/du-an.html':'142207',
'https://angia.com.vn/vi/du-an.html':'142208',
'https://www.youtube.com/c/AngiaVn':'142209',
'https://www.youtube.com/c/AngiaVn':'142210',
'https://angia.com.vn/detect.html':'142211',
'https://angia.com.vn/detect.html':'142212',
'http://www.w3.org/2000/svg':'142213',
'http://www.w3.org/2000/svg':'142214',
'http://www.w3.org/2000/svg':'142215',
'http://www.w3.org/2000/svg':'142216',
'http://www.w3.org/2000/svg':'142217',
'http://www.w3.org/2000/svg':'142218',
'http://www.w3.org/2000/svg':'142219',
'http://www.w3.org/2000/svg':'142220',
'https://angia.com.vn/':'142221',
'https://angia.com.vn/':'142222',
'https://angia.com.vn/':'142223',
'https://angia.com.vn/':'142224',
'http://schema.org':'142225',
'http://www.btq.vn':'142226',

}

if __name__ == '__main__':
    replace('cungduong.html', my_dict)
