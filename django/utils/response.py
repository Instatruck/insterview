from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

class CustomResponse:
    def __init__(self, status_code:status, data=None, message="", headers={}, pagination:Paginator=None, page:int=1, page_size:int=5)->Response:
        self.data = data
        self.message = message
        self.headers = headers
        self.pagination = pagination
        self.page = page
        self.page_size = page_size
        self.status_code = status_code
        

    def to_json_response(self):
        response_data = {"status": self.status_code, "message": self.message, "data": self.data}
        if self.pagination != None :
            data_on_page = self.pagination.page(self.page)
            page_meta = {
                "page":  self.page,
                "page_size": self.page_size,
                "total_pages": self.pagination.num_pages,
                "has_next": data_on_page.has_next(),
                "has_previous": data_on_page.has_previous()
            }
            response_data['pagination'] = page_meta

        return Response(response_data,
                        status=self.status_code, headers=self.headers, content_type='application/json; charset=utf-8')
