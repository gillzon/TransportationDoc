
def generate_label(data):
    print(data.printertype)
    label = """^XA
                ^SZ2^JMA
                ^MCY^PMN
                ^PW812
                ~JSN
                ^JZY
                ^LH0,0^LRN
                ^XZ
                ^XA
                ^FT23,161
                ^CI28
                ^A0N,28,29^FDFrom:^FS
                ^FO0,113
                ^GB812,3,3^FS
                ^FT48,79
                ^A0N,56,76^FDPALLET^FS
                ^FT101,161
                ^A0N,28,25^FD{site_name}^FS
                ^FT101,193
                ^A0N,28,25^FD{site_address}^FS
                ^FT101,224
                ^A0N,28,25^FD{site_zipcode} - {site_city}^FS
                ^FT101,256
                ^A0N,28,25^FD{site_country}^FS
                ^FO24,303
                ^GB3,52,3^FS
                ^FO25,303
                ^GB50,3,3^FS
                ^FO738,303
                ^GB51,3,3^FS
                ^FO787,304
                ^GB3,51,3^FS
                ^FO787,453
                ^GB3,52,3^FS
                ^FO738,503
                ^GB50,3,3^FS
                ^FO24,503
                ^GB51,3,3^FS
                ^FO24,453
                ^GB3,51,3^FS
                ^FO0,281
                ^GB811,3,3^FS
                ^FT48,360
                ^A0N,28,29^FDTo:^FS
                ^FT96,361
                ^A0N,34,33^FD{rcv_name}^FS
                ^FT96,400
                ^A0N,34,33^FD{rcv_address}^FS
                ^FT96,439
                ^A0N,34,33^FD{rcv_zipcode} - {rcv_city}^FS
                ^FT96,473
                ^A0N,34,33^FD{rcv_isocountry}^FS
                ^FO106,643
                ^BY3^BCN,201,N,N^FD>:{unit_identifier}^FS
                ^FT211,876
                ^A0N,34,46^FD{unit_identifier}^FS
                ^FT23,1188
                ^A0N,23,22^FD© 2022 CCS - The Open Source Carrier Core System ^FS
                ^FO238,923
                ^BCN,169,N,N^FD>:SE-4>{rcv_zipcode}^FS
                ^FT307,1124
                ^A0N,34,46^FDSE-{rcv_zipcode}^FS
                ^FT595,357
                ^A0N,23,22^FDContact:^FS
                ^FT595,380
                ^A0N,23,22^FD{rcv_contact}^FS
                ^FT23,543
                ^A0N,28,27^FDRef: {unit_identifier}^FS
                ^FT23,577
                ^A0N,28,27^FDShpRef: DJFKRI3223^FS
                ^FT535,260
                ^A0N,34,33^FDWeight: {unit_weight} Kg^FS
                ^FT23,612
                ^A0N,28,27^FDDesc: fragile^FS
                ^FT48,110
                ^A0N,14,13^FDGen: 2022-01-12 ^FS
                ^FT544,174
                ^A0N,42,37^FDPcs: {unit_counter} / {shipment_parcel_count}^FS
                ^FT493,543
                ^A0N,28,27^FDPickupDate: 2021-12-01^FS
                ^FT493,577
                ^A0N,28,27^FDType: glass^FS
                ^FT493,612
                ^A0N,28,27^FDItem/nr: 2^FS
                ^FO544,25
                ^XGR:SSGFX000.GRF,1,1^FS
                ^PQ1,0,1,Y
                ^XZ
                ^XA
                ^XZ""".format(
        rcv_address=data.receiver.address1,
        rcv_address2=data.receiver.address2,
        rcv_zipcode=data.receiver.zipcode,
        rcv_city=data.receiver.city,
        rcv_isocountry=data.receiver.isocountry,
        rcv_name=data.receiver.name,
        rcv_contact=data.receiver.contact,
        site_address=data.sender.address1,
        site_address2=data.sender.address2,
        site_name=data.sender.name,
        site_zipcode=data.sender.zipcode,
        site_city=data.sender.city,
        site_country=data.sender.isocountry,
        shipment_service=str(data.service).upper(),
        shipment_parcel_count=data.unitNumber,
        unit_identifier=data.trackingId,
        unit_weight=data.weight,
        unit_counter=data.unitNumber,
    )
    return label


def generate_label_portal(data, totalshp, parcelnumber):
    if parcelnumber == 0:
        parcelnumber = 1
    print(data['parcel'])
    label = """^XA
                ^SZ2^JMA
                ^MCY^PMN
                ^PW812
                ~JSN
                ^JZY
                ^LH0,0^LRN
                ^XZ
                ~DGR:SSGFX000.GRF,1701,27,7FFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC0000000000F800000000001F000001F0000000FFFFF80FFFFFFFFC0000000000F800000000001F000001F0000000FFFFF80FFFFFFFFC0000000000F800000000001F000001F0000000FFFFF80FFFFFFFFC0000000000F800000000001F000001F0000000FFFFF80FFFFFFFFC0000000000F800000000001F000001F0000000FFFFF80FFFFFFFFC0000000000F800000000001F000001F0000000FFFFF80FFFFFFFFC000000000000000000000000000001F0000000FFFFF80FFFFFFFFC000000000000000000000000000001F0000000FFFFF80FFFFFFFFC000000000000000000000000000001F0000000FFFFF80FFFFFFFFC00000FF00000001F80000000000F81F0007E00FFFFF80FFFFFFFFC00003FFC00F87C7FE00FFF1F003FE1F003FF80FFFFF807FFFFFFFC0000FFFF00F87CFFF01FFF1F00FFF9F00FFFE0FFFFFC03FFFFFFFC0001FFFF80F87FFFF81FFF1F01FFFFF01FFFF0FFFFFC01FFFFFFFC0003FC3FC0F87FFFFC1FFF1F03FFFFF03FE7F8FFFFFE01FFFFFFFC0003F00FC0F87F80FC1F001F07F01FF03F00FCFFFFFF00FFFFFFFC0007E007E0F87F007E1F001F07E007F07C007CFFFFFF807FFFFFFC000FC003E0F87E007E1F001F07C007F0FC003EFFFFFFC03FFFFFFC000F8001F0F87E003E1F001F0FC003F0F8003EFFFFFFC01FFFFFFC000F8001F0F87C003E1F001F0F8003F0F8001FFFFFFFE00FFFFFFC001F8001F0F87C003E1F001F0F8001F1F8001FFFFFFFF007FFFFFC001FFFFFF0F87C003E1F001F1F8001F1FFFFFFFFFFFFF803FFFFFC001FFFFFF0F87C003E1F001F1F8001F1FFFFFFFFFFFFFC03FFFFFC001FFFFFF0F87C003E1F001F1F8001F1FFFFFFFFFFFFFE01FFFFFC001FFFFFF0F87C003E1F001F1F8001F1FFFFFFFFFFFFFE00FFFFFC001F800000F87C003E1F001F1F8001F1FFFFFFFFFFFFFF007FFFFC001F800000F87C003E1F001F1F8001F1F00000FFFFFFFF807FFFFC001F800000F87C003E1F001F0F8001F1F80000FFFFFFFFC07FFFFC000F800000F87C003E1F001F0F8003F0F80000FFFFFFFFE07FFFFC000FC001F0F87C003E1F001F0FC003F0F8001FFFFFFFFFE07FFFFC000FC003F0F87C003E1F001F07C007F0FC003FFFFFFFFFE07FFFFC0007E003E0F87C003E1F001F07E007F07E007EFFFFFFFFE07FFFFC0003F80FE0F87C003E1F001F03F81FF03F00FCFFFFFFFFE07FFFFC0003FFFFC0F87C003E1F001F03FC7FF03FFFFCFFFFFFFFE07FFFFC0001FFFF80F87C003E1F001F01FFFFF01FFFF8FFFFFFFFE03FFFFC00007FFF00F87C003E1F001F00FFF9F007FFE0FFFFFFFFE03FFFFC00003FFC00F87C003E1F001F007FF1F003FFC0FFFFFFFFE03FFFFC000003E0000000000000000000078000003E00FFFFFFFFE03FFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000FFFFFFFFFFFFFFFC00000000000000000000000000000000000000
                ^XA
                ^FT23,161
                ^CI28
                ^A0N,28,29^FDFrom:^FS
                ^FO0,113
                ^GB812,3,3^FS
                ^FT48,79
                ^A0N,56,76^FDPALLET^FS
                ^FT101,161
                ^A0N,28,25^FD{site_name}^FS
                ^FT101,193
                ^A0N,28,25^FD{site_address}^FS
                ^FT101,224
                ^A0N,28,25^FD{site_zipcode} - {site_city}^FS
                ^FT101,256
                ^A0N,28,25^FD{site_country}^FS
                ^FO24,303
                ^GB3,52,3^FS
                ^FO25,303
                ^GB50,3,3^FS
                ^FO738,303
                ^GB51,3,3^FS
                ^FO787,304
                ^GB3,51,3^FS
                ^FO787,453
                ^GB3,52,3^FS
                ^FO738,503
                ^GB50,3,3^FS
                ^FO24,503
                ^GB51,3,3^FS
                ^FO24,453
                ^GB3,51,3^FS
                ^FO0,281
                ^GB811,3,3^FS
                ^FT48,360
                ^A0N,28,29^FDTo:^FS
                ^FT96,361
                ^A0N,34,33^FD{rcv_name}^FS
                ^FT96,400
                ^A0N,34,33^FD{rcv_address}^FS
                ^FT96,439
                ^A0N,34,33^FD{rcv_zipcode} - {rcv_city}^FS
                ^FT96,473
                ^A0N,34,33^FD{rcv_isocountry}^FS
                ^FO106,643
                ^BY3^BCN,201,N,N^FD>:{parcel_identifier}^FS
                ^FT211,876
                ^A0N,34,46^FD{parcel_identifier}^FS
                ^FT23,1188
                ^A0N,23,22^FD© 2021 Einride - intelligent technologies for movement ^FS
                ^FO238,923
                ^BCN,169,N,N^FD>:SE-4>{rcv_zipcode}^FS
                ^FT307,1124
                ^A0N,34,46^FDSE-{rcv_zipcode}^FS
                ^FT595,357
                ^A0N,23,22^FDContact:^FS
                ^FT595,380
                ^A0N,23,22^FD{rcv_contact}^FS
                ^FT23,543
                ^A0N,28,27^FDRef: {parcel_identifier}^FS
                ^FT23,577
                ^A0N,28,27^FDShpRef: {shp_reference}^FS
                ^FT535,260
                ^A0N,34,33^FDWeight: {parcel_weight} Kg^FS
                ^FT23,612
                ^A0N,28,27^FDDesc: {parcel_description}^FS
                ^FT48,110
                ^A0N,14,13^FDGen: {parcel_gendate} ^FS
                ^FT544,174
                ^A0N,42,37^FDPcs: {parcel_counter} / {shipment_parcel_count}^FS
                ^FT493,543
                ^A0N,28,27^FDPickupDate: 2021-12-01^FS
                ^FT493,577
                ^A0N,28,27^FDType: {parcel_itemType}^FS
                ^FT493,612
                ^A0N,28,27^FDItem/nr: {parcel_itemnr}^FS
                ^FO544,25
                ^XGR:SSGFX000.GRF,1,1^FS
                ^PQ1,0,1,Y
                ^XZ
                ^XA
                ^IDR:SSGFX000.GRF^XZ
                """.format(
        rcv_address=data['receiver']['address'],
        rcv_zipcode=data['receiver']['postalCode'],
        rcv_city=data['receiver']['city'],
        rcv_isocountry=data['receiver']['countryCode'].upper(),
        rcv_name=data['receiver']['displayName'],
        rcv_contact=data['receiver']['displayName'],
        site_address=data['site']['address'],
        site_name=data['site']['displayName'],
        site_zipcode=data['site']['postalCode'],
        site_city=data['site']['city'],
        site_country=data['site']['countryCode'],
        shipment_parcel_count=totalshp,
        parcel_identifier=data['parcel']['referenceId'],
        parcel_weight=data['parcel']['weightKilograms'],
        parcel_description=data['parcel']['description'],
        parcel_gendate=data['parcel']['createTime'],
        parcel_itemType=data['parcel']['itemType'],
        parcel_itemnr=data['parcel']['itemNumber'],
        parcel_counter=parcelnumber,
        shp_reference=data['parcel']['shipmentReferenceId']
    ).replace("\n", " ")
    return label
