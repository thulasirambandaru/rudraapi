from apiDB import db
from flask import jsonify
from flask_restful import Resource, reqparse
from models.ManufactureOrdersModel import ManufactureOrderModel

parser = reqparse.RequestParser()
parser.add_argument('productID', type=int, required=False)
parser.add_argument('quantity', type=str, required=False)
parser.add_argument('specification', type=str, required=False)
parser.add_argument('orderStatus', type=int, required=False)
parser.add_argument('notes', type=str, required=False)
parser.add_argument('createdBy', type=int, required=False)
parser.add_argument('updatedBy', type=int, required=False)


class ManufactureOrdersData(Resource):
    def getOrders(self):
        records = ManufactureOrderModel.query.all()
        return jsonify([ManufactureOrderModel.serialize(record) for record in records])

    def getOrderItem(self, orderID):
        return jsonify(ManufactureOrderModel.serialize(ManufactureOrderModel.query.\
               filter_by(mID=orderID).first_or_404(description='Record with id={} is not available'.format(orderID))))

    def createOrder(self):
        args = parser.parse_args(strict=True)
        record = ManufactureOrderModel()
        record.productID = args['productID']
        record.quantity = args['quantity']
        record.specification = args['specification']
        record.orderStatus = args['orderStatus']
        record.notes = args['notes']
        record.createdBy = args['createdBy']
        db.session.add(record)
        db.session.commit()
        return ManufactureOrderModel.serialize(record), 201

    def updateOrderItem(self, orderID):
        args = parser.parse_args(strict=True)
        record = ManufactureOrderModel.query.filter_by(mID=orderID).\
                 first_or_404(description='Record with id={} is not available'.format(orderID))
        record.productID = args['productID']
        record.quantity = args['quantity']
        record.specification = args['specification']
        record.orderStatus = args['orderStatus']
        record.notes = args['notes']
        record.updatedBy = args['updatedBy']
        db.session.commit()
        return ManufactureOrderModel.serialize(record), 201

    def deleteOrderItem(self, orderID):
        record = ManufactureOrderModel.query.filter_by(mID=orderID)\
            .first_or_404(description='Record with id={} is not available'.format(orderID))
        db.session.delete(record)
        db.session.commit()
        return '', 204
