from flask import Flask
from flask_restful import Api
from Resources.fetch import Fetch
from Resources.pay import Pay

app = Flask(__name__)
api = Api(app)


# Resources end point
api.add_resource(Fetch, "/setu/fetch")
api.add_resource(Pay, "/setu/pay")

if __name__ == "__main__":
    app.run(port=5000)
