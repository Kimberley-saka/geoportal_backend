import json
import psycopg
import tempfile
from rest_framework.decorators import APIView
from rest_framework.response import Response
from osgeo import ogr



class getGeospatialData(APIView):
    """
    __get spatial data from the database
    """

    def get(self, request, *args, **kwargs):
        """
        retreive spatial data given user parameters
        """

        search_param = request.data.get('search')

        connection = psycopg.connect(
            dbname='geoportal',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )


        tmpfile = 

      