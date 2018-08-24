from pydal import DAL, Field

dbConnect = DAL('mysql://root:root@localhost/mydatabase')

try:
    #The syntax to create order table and insert data in it
    dbConnect.define_table('order', Field('userId',required=True) ,
                           Field('ngaymua', type='date'),
                           Field('name', type='text'),
                           Field('age', type='integer'),
                           Field('phone', type='text'),
                           Field('email', type='text'),
                           Field('cach_thanh_toan', type='text'),
                           Field('phuong_thuc_nhan', type='text'),
                           Field('quan_huyen', type='text'),
                           primarykey=['userId']
                           )

    # The syntax to create order detail table and insert data in it
    dbConnect.define_table('order_detail', Field('eventId', required=True),
                           Field('userId', required=True),
                           Field('name_event', type='text'),
                           Field('diadiem_tochuc', type='text'),
                           Field('thoigian_tochuc', type='datetime'),
                           Field('quan_huyen_tochuc', type='text'),
                           primarykey=['eventId','userId']
                           )

    dbConnect.order.insert(userId = 'KH002' ,ngaymua = '2018/05/08',name = 'Nguyen Van B',age = 26,
                           phone = '01234569856', email = 'Bnv@gmail.com', cach_thanh_toan = 'Qua ATM' ,
                           phuong_thuc_nhan = "Truc Tiep" , quan_huyen = 'Hai Chau')
    dbConnect.order.insert(userId='KH003', ngaymua='2018/03/08', name='Nguyen Van C', age=23,
                           phone='01234569456', email='Cnv@gmail.com', cach_thanh_toan='Qua ATM',
                           phuong_thuc_nhan="Truc Tiep", quan_huyen='Lien Chieu')
    dbConnect.order.insert(userId='KH004', ngaymua='2018/02/08', name='Nguyen Van D', age=24,
                           phone='09234569876', email='Dnv@gmail.com', cach_thanh_toan='Qua ATM',
                           phuong_thuc_nhan="Truc Tiep", quan_huyen='Lien Chieu 2')
    dbConnect.order_detail.insert(eventId = "EV001",userId='KH001', name_event='Phao Hoa 30/4',
                                  diadiem_tochuc='Nha Van Hoa Lien Chieu'
                                  , thoigian_tochuc='2018/06/07 13:23', quan_huyen_tochuc='Lien Chieu')
    dbConnect.order_detail.insert(eventId="EV001", userId='KH002', name_event='Phao Hoa 30/4',
                                  diadiem_tochuc='Nha Van Hoa Lien Chieu'
                                  , thoigian_tochuc='2018/06/07 13:23', quan_huyen_tochuc='Lien Chieu')


finally:
    if dbConnect:
        dbConnect.close()
