from pydal import DAL, Field

dbConnect = DAL('mysql://root:root@localhost/studyCode')

try:
    #The syntax to create order table and insert data in it
    dbConnect.define_table('order', Field('userId',required=True) ,
                           Field('ngaymua', type='date'),
                           Field('name', type='text'),
                           Field('event_name', type='text'),
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

    # The syntax to create order detail table and insert data in it
    dbConnect.define_table('list_event', Field('event_name' ,type = 'text'),
                           Field('dia_diem', type = 'text'),
                           Field('thoi_gian', type='date'),
                           )
    # dbConnect.list_event.insert(event_name = 'Phao Hoa',dia_diem = 'Cau rong',thoi_gian = '2018/05/06')
    # dbConnect.list_event.insert(event_name='Cau phun lua', dia_diem='Cau rong', thoi_gian='2018/05/07')
    # dbConnect.list_event.insert(event_name='Duong pho', dia_diem='Hai Chau', thoi_gian='2018/05/06')
    # dbConnect.order.insert(userId = 'KH002' ,ngaymua = '2018/05/08',name = 'Nguyen Van B',event_name = 'Phao Hoa',
    #                        age = 26,phone = '01234569856', email = 'Bnv@gmail.com', cach_thanh_toan = 'Qua ATM' ,
    #                        phuong_thuc_nhan = "Truc Tiep" , quan_huyen = 'Hai Chau')
    # dbConnect.order.insert(userId='KH003', ngaymua='2018/03/08', name='Nguyen Van C',event_name = 'Phao Hoa', age=23,
    #                        phone='01234569456', email='Cnv@gmail.com', cach_thanh_toan='Qua ATM',
    #                        phuong_thuc_nhan="Truc Tiep", quan_huyen='Lien Chieu')
    # dbConnect.order.insert(userId='KH004', ngaymua='2018/02/08', name='Nguyen Van D', event_name = 'Phao Hoa', age=24,
    #                        phone='09234569876', email='Dnv@gmail.com', cach_thanh_toan='Qua ATM',
    #                        phuong_thuc_nhan="Truc Tiep", quan_huyen='Lien Chieu 2')
    # dbConnect.order_detail.insert(eventId = "EV001",userId='KH001', name_event='Phao Hoa 30/4',
    #                               diadiem_tochuc='Nha Van Hoa Lien Chieu'
    #                               , thoigian_tochuc='2018/06/07 13:23', quan_huyen_tochuc='Lien Chieu')
    # dbConnect.order_detail.insert(eventId="EV001", userId='KH002', name_event='Phao Hoa 30/4',
    #                               diadiem_tochuc='Nha Van Hoa Lien Chieu'
    #                               , thoigian_tochuc='2018/06/07 13:23', quan_huyen_tochuc='Lien Chieu')

    #This method to get all event is da nang city
    def list_festival():
        getAllEvents = dbConnect().select(dbConnect.list_event.ALL)
        for events in getAllEvents :
            print('Name :',events['event_name'] ,': Address :',events['dia_diem'] ,': Time :',events['thoi_gian'])

    #This method to regist new member to join event
    def regist_member():
        print("Plase input your ID:")
        userId = str(input())
        print("Plase input Ngay mua:")
        ngaymua = str(input())
        print("Plase input your name:")
        name = str(input())
        print("Plase input the name of event:")
        event_name = str(input())
        print("Plase input your age :")
        age = int(input())
        print("Plase input your phone number:")
        phone = str(input())
        print("Plase input your Email:")
        email = str(input())
        print("Plase input way to pay:")
        cach_thanh_toan = str(input())
        print("Plase input way to receive:")
        phuong_thuc_nhan = str(input())
        print("Plase input Address :")
        quan_huyen = str(input())
        dbConnect.order.insert(userId='%s'%userId, ngaymua='%s'%ngaymua, name='%s'%name, event_name ='%s'%event_name,
                               age='%r'%age,phone='%s'%phone, email='%s'%email, cach_thanh_toan='%s'%cach_thanh_toan,
                          phuong_thuc_nhan='%s'%phuong_thuc_nhan, quan_huyen='%s'%quan_huyen)
        print("Your regist is success!")

    #This method to list all pepple join the event
    def list_registed():
        getListRegisted = dbConnect(dbConnect.order.userId == dbConnect.order_detail.userId).select()
        for listRegist in getListRegisted:
            print(listRegist.order.userId,listRegist.order_detail.eventId)

    #This method to find the people hava been registed
    def list_registedById():
        getListRegisted = dbConnect(dbConnect.order.userId == dbConnect.order_detail.userId).select()
        print("Please input Id need to find")
        userId = str(input())
        for data in getListRegisted.find(lambda data: data.order.userId[0] == '%s'%userId):
            print(data.order.userId, data.order_detail.eventId)

    print("You Want to regist in event!input 1 >> ok 2 >> not ")
    check = int(input())
    while check < 4:
        print("Welcome to festival in Da nang city!")
        print("       ---------------------     ")
        print("You can choose the option!")
        print("You are 1 : member or 2: not member or 3 :find 4 :delete ..> 5to exist")

        position = int(input())

        if position == 1:
            print("--List of festival in Da Nang city---")
            list_festival()
        elif position == 2:
            print("--Please regist member--")
            regist_member()
        elif position == 3:
            print("--List the people have been registed--")
            list_registedById()
        elif position == 4:
            print("--List the people have been registed by Id--")
            list_registed()
        else :
            check = 3
finally:
    if dbConnect:
        dbConnect.close()
