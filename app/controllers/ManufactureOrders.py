
from flask_restful import Resource
from modules.ManufactureOrdersData import ManufactureOrdersData

class ManufactureOrders(Resource):
    def __init__(self):
        self.moObj = ManufactureOrdersData()

    def get(self):
        return self.moObj.getOrders()

    def post(self):
        return self.moObj.createOrder()


class ManufactureOrderItems(Resource):
    """ This class is used for mo_order table end points """
    def __init__(self):
        self.moObj = ManufactureOrdersData()

    def get(self, orderID):
        return self.moObj.getOrderItem(orderID)

    def put(self, orderID):
        return self.moObj.updateOrderItem(orderID)

    def delete(self, orderID):
        return self.moObj.deleteOrderItem(orderID)
