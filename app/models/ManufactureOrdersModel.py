
from apiDB import db
from datetime import date, datetime
from sqlalchemy import Column, Integer, DateTime, String
from json import dumps

class ManufactureOrderModel(db.Model):
    """Define Sqlalchemy elements for DB tables and relationships."""
    __tablename__ = 'mo_order'

    mID = Column('mo_order_id', Integer, primary_key=True)
    productID = Column('product_id', Integer)
    quantity = Column('quantity', String(45))
    specification = Column('specification', String(500))
    orderStatus = Column('order_status', Integer, default=1)
    notes = Column('notes', String(1000))
    createdBy = Column('created_by', Integer)
    updatedBy = Column('updated_by', Integer)
    created = Column('created', DateTime, default=datetime.now())
    updated = Column('updated', DateTime, default=datetime.now())

    def jsonSerial(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError ("Type %s not serializable" % type(obj)) 

    def serialize(self):
        return {
            'mo_order_id': self.mID,
            'product_id': self.productID,
            'quantity': self.quantity,
            'specification': self.specification,
            'order_status': self.orderStatus,
            'notes': self.notes,
            'created_by': self.createdBy,
            'updated_by': self.updatedBy,
            'created': dumps(self.created, default=self.jsonSerial),
            'updated': dumps(self.updated, default=self.jsonSerial)
        }

    __mapper_args__ = {'primary_key':[mID]}
    

    def __init__(self):
        pass