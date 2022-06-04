

def get_data_from_post(request, fields):
    form_data=dict()
    for field in fields:
        value=request.POST.get(field)
        form_data[field]=value
    return form_data