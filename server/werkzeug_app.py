#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response
import json

@Request.application
def application(request):
    print(f"This web server is running at {request.remote_addr}")
    print(f"Method: {request.method}, Path: {request.path}")
    print(f"Query args: {request.args}")
    print(f"User-Agent: {request.headers.get('User-Agent')}")
    body = request.get_data(as_text=True)
    if body:
        print(f"Body:", body)

    name = request.args.get("name")
    if name:
        return Response(f"Hello, {name}! This WSGI generated this response!", mimetype="text/plain")

    
    if request.path == "/json":
        payload = {"message": "Hello from WSGI", "method": request.method}
        return Response(json.dumps(payload), mimetype="application/json")
    
    return Response("A WSGI generated this response!", mimetype="text/plain")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple(
        hostname="localhost",
        port=5555,
        application=application,
        use_debugger=True,
        use_reloader=True
    )
    