import pdb
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

data_dict = {}

def initialize(blacklist):
    with open(blacklist) as f:
        for line in f:
            cols = [x for x in line.split(' ')]
            data_dict[cols[1].replace('\n','')] = cols[0]

"""
I think phone number for every user is unique. But lets check the name too.
"""
def check_blacklist(name, phone):
    if phone in data_dict and data_dict[phone] == name:
        return True
    return False

@Request.application
def application(request):
    path = request.path
    if path == '/blacklist':
        name = request.args.get('name')
        phone = request.args.get('phone')
        if phone is not None and name is not None:
            return Response("%r" % check_blacklist(name, phone), status=200)
        return Response("Bad Request", status=400)
    return Response("Not Found", status=404)


if __name__ == '__main__':
    initialize('files/blacklist.txt')
    run_simple('127.0.0.1', 3000, application)