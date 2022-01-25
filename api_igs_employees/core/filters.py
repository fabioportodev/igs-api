
def filter_queryparams(request, queryset):

    if 'name' in request.query_params:
        queryset = queryset.filter(name__icontains=request.query_params.get('name'))
    if 'email' in request.query_params:
        queryset = queryset.filter(email__icontains=request.query_params.get('email'))
    if 'departament' in request.query_params:
        queryset = queryset.filter(departament__name__icontains=request.query_params.get('departament'))

    return queryset