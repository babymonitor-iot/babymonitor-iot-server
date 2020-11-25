import os


def validate_request(request):
    funcs = [
        validate_empty_request,
        validate_request_fields,
        validate_file_type
    ]
    for func in funcs:
        validate, msg = func(request)
        if not validate:
            return validate, msg

    return True, 'OK'

def validate_empty_request(request):
    if not request.form:
        return False, 'Empty request'

    return True, 'OK'


def validate_request_fields(request):
    if not request.files:
        return False, 'No file found'
  
    if 'service_type' not in request.form:
        return False, 'No service type found'
 
    return True, 'OK'


def validate_file_type(request):
    file = request.files['file']
    filetype = file.filename.split('.')[1]

    if filetype != 'rrd':
        return False, 'Wrong file format'

    return True, 'OK'


def validate_file_is_empty(request):
    # file = request.files['file']
    # file.seek(0, os.SEEK_END)
    # file_length = file.tell()
    # if file_length == 0:
    #     return False, 'File is empty'

    return True, 'OK'
