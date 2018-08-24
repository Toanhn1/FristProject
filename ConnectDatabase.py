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



finally:
    if dbConnect:
        dbConnect.close()
