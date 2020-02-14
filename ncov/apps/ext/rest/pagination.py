from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination as drf_PageNumberPagination
from rest_framework.response import Response


class PageNumberPagination(drf_PageNumberPagination):
    def get_paginated_response(self, data):
        ret = OrderedDict(
            [
                ("next", self.get_next_link()),
                ("previous", self.get_previous_link()),
                ("results", data),
            ]
        )
        return Response(data=ret)

