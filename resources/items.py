import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items,stores
from schemas import ItemsSchema, ItmesUpdateScehma

blp = Blueprint("items", __name__ , description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self,item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="item not found")
    
    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message": "Item Deleted Successfully"}
        except KeyError:
            abort(404, message="item not found")
    
    @blp.arguments(ItmesUpdateScehma)
    def put(self, item_data, item_id):
       
        if item_id in items:
            items[item_id]["price"] = item_data["price"]
            items[item_id]["name"] = item_data["name"]
            return items[item_id], 200

        abort(404, message="item with this id not found")


@blp.route("/item")
class itemList(MethodView):

    @blp.arguments(ItemsSchema)
    def post(self, item_data):


        #item_data = request.get_json()  now we dont use this it will get validated gata from 2nd parameter

        #marshamallow can only check the incoming data 
        #using schema to check incoming data
    

        #also check wheather item name and store id should not be duplicate

        for item in items.values():
            if item_data["store_id"] == item["store_id"] and item_data["name"] == item["name"]:
                abort(
                    404,
                    message="Duplicate items found"
                )

        if item_data["store_id"] not in stores:
            abort(404, message="store not found")
        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201
    
    def get(self):
        return {"items": list(items.values())}