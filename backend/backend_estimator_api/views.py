from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend_estimator_api.estimator import estimator


class Estimator(APIView):
    """
    """

    def post(self, request):
        """
        Return a list of all users.
        """
        data = request.data
        res = estimator(data)
        return Response(res, status=status.HTTP_200_OK)
