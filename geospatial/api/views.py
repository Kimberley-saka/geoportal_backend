from rest_framework.decorators import APIView
import requests
import json
from rest_framework import status
from rest_framework.response import Response

class getGeoData(APIView):
    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get('searchTerm')

        geoserver_url = 'http://localhost:8090/geoserver/rest/workspaces/shapefiles/datastores/geoportal/featuretypes'
        response = requests.get(geoserver_url)
        if response.status_code == 200:
            try:
                shapefile_info = response.json()
                return Response(shapefile_info, status=status.HTTP_200_OK)
            except json.JSONDecodeError:
                return Response({"error": "Invalid JSON received"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": f"Received status code {response.status_code}"})

        
        
        
        shapefile_data = requests.get(download_url).content


        geojson_response = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": json.loads(shapefile_data),
                    "properties": {},
                }
            ]
        }

        return Response(geojson_response)

    
