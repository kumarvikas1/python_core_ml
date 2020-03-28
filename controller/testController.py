from sanic import Sanic
from sanic.response import json
from sanic.log import logger
from sanic_prometheus import monitor

app = Sanic()
monitor(app).expose_endpoint()

#python3 -m controller.testController
#Create a lib called core_platform and then all the different models extentend and run it
#Core lib should post to kafka request and response received

def test1(executor):
    @app.route("/")
    async def test(request):
        print(request.json)
        return json({"hello": "world"})

    @app.route("/post", methods = ['POST'])
    async def testp(request):
        print(request.json['name'])
        return json({"hello": "world"})

    @app.route("/postModel", methods = ['POST'])
    async def testpsd(request):
        print(request.json)
        return json({"prediction": executor.executeModel(request)})

    @app.route("/model")
    async def test(request):
        return json({"prediction": executor.executeModel(request)})

    app.run(host="0.0.0.0", port=8000)


