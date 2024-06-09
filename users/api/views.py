from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_routes(request):
    """
    show all available routes
    """
    routes = [
        {
        'detail': '/api/users/<int:id>/',
        'create': '/api/users/create/',
        'update': '/api/users/update/<int:id>/',
        'delete': '/api/users/delete/<int:id>/',
        },
        ]
    return Response(routes)