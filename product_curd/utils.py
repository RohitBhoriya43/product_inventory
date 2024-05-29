from rest_framework.response import Response

def set_response(success,data,message,status):

    res= {
        "success":success,
        "data":data,
        "message":message
    }

    return Response(res,status)