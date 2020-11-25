def construct_response(type, msg, to=''):
	if to:
	    return {
	        'type': type,
	        'msg': msg,
	        'route': {
	        	'from': 'tv',
	        	'to': to,
	        }
	    }

	else:
	    return {
	        'type': type,
	        'msg': msg,
	    }
