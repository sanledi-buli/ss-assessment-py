import pdb
from werkzeug.wrappers import Request, Response

arr_dict = []

def initialize(blacklist):
    with open(blacklist) as f:
        for line in f:
            cols = [x for x in line.split(' ')]
            arr_dict.append({'name' : cols[0], 'phone' : cols[1].replace('\n','')})

"""
I think phone number for every user is unique. But lets check the name too.
"""
def check_blacklist(name, phone):
    return any(d['phone'] == phone and d['name'] == name for d in arr_dict)

@Request.application
def application(request):
    path = request.path
    if path == '/blacklist':
        name = str(request.args.get('name'))
        phone = str(request.args.get('phone'))
        if phone is not None and name is not None:
            return Response("%r" % check_blacklist(name, phone))
        return Response("False")


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    initialize('blacklist.txt')
    run_simple('127.0.0.1', 3000, application)