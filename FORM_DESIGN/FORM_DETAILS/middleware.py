def FORM_DESIGN_middleware(get_response):
    print("code executed only once for any initialization")

    def FORM_DESIGN_function(request):
        print("code executed before view function is called")
        res=get_response(request)
        print("code executed after view function is called")
        return res
    return FORM_DESIGN_function