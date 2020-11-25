def check_request_source(request):
    
    try: 
        return request.user_agent.browser.lower()
    except:
        return ''
