from django.db import models
from django.core.paginator import Paginator

def GetPageAndPageSizeFromRequest(request):
    page = request.GET.get('page', 1)
    try: 
        page =  int(page)
    except ValueError:
        page = 1

    page_size = request.GET.get('page-size', 5)
    try: 
        page_size = int(page_size)
    except ValueError:
        page_size = 5
    return page, page_size