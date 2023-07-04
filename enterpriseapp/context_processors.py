from .views import header_footer_data

def header_footer_context(request):
    return {'header_footer_data': header_footer_data()}