class Product():

    def __init__(self,prid=0,prnm='',price=0,prven='',prqty=0):

        self.Product_ID=int(prid)
        self.Product_Name=prnm
        self.Product_Price=float(price)
        self.Product_Vendor=prven
        self.Product_Qty=int(prqty)


    def __str__(self):
        return  f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)