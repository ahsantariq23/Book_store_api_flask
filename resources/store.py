import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoresSchema

#blueprint divides api in multiple segments makes modular
blp = Blueprint("stores", __name__ , description="Operations on Store")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store Deleted"}
        except KeyError:
            abort(404, message="Store not found")

@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}
    
    @blp.arguments(StoresSchema)
    def post(self, store_data):
        # request_data=request.get_json()
        # store_addition={"name":request_data["name"],"items":[]}
        # stores.append(store_addition)
        # return stores, 201
        
        #we cant use marshmallow to check the existing data with incoming so we have do that here 
        #checking if the store already exists or not
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(
                    404,
                    message="Bad .Request Name should be included in json payload"
                )
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201