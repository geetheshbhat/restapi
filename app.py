from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from db import db


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item,Itemlist
from resources.store import Store, StoreList

app=Flask(__name__)
app.secret_key="geethesh"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
jwt=JWT(app,authenticate,identity)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)