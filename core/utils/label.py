
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
