import json
import psycopg2
from rest_framework.decorators import APIView
from rest_framework.response import Response



class getGeospatialData(APIView):
    """
    __get spatial data from the database
    """

    def get(self, request, *args, **kwargs):
        """
        retreive spatial data given user parameters
        """

        search_param = request.data.get('search')

        connection = psycopg2.connect(
            dbname='geoportal',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )

      