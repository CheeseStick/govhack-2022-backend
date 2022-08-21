from rest_framework import pagination


class PipeListPagination(pagination.PageNumberPagination):
    page_size = 100
