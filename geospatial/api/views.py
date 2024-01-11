from rest_framework.decorators import APIView
import requests
import json
from rest_framework import status
from rest_framework.response import Response

class getGeoData(APIView):
    def get(self, request, *args, **kwargs):
        search_term = request.data.get('searchTerm')

        geoserver_url = 'localhost:8080/geoserver/rest/workspaces/shapefiles/datastores/shapefiles/featuretypes'
        response = requests.get(geoserver_url)
        shapefile_info = response.json()

        for feature_type in shapefile_info['featureTypes']:
            if feature_type['name'] == search_term:
                download_url = feature_type['links'][1]['href']
                break
        
        else:
            return Response({'detail: data not found'}, status=status.HTTP_404_NOT_FOUND)
        
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

    
