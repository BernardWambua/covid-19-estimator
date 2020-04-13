from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend_estimator_api.estimator import estimator


class Estimator(APIView):
    """
    """

    def post(self, request):
        """
        Return data as well as impact and severe impact estimations.
        """
        data = request.data
        res = estimator(data)
        return Response(res, status=status.HTTP_200_OK)
