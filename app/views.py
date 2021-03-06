# from rest_framework.parsers import FileUploadParser
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status

# from .serializers import FileSerializer


# class FileUploadView(APIView):
#     parser_class = (FileUploadParser,)

#     def post(self, request, *args, **kwargs):

#       file_serializer = FileSerializer(data=request.data)
#       print(file_serializer)

#       if file_serializer.is_valid():
#           file_serializer.save()
#           return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#       else:
#           return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
import sys
sys.path.append("..")
from media import utils
import os


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            # print(file_serializer.data['file'])
            path1 = file_serializer.data['file']
            p = path1.split(os.sep)
            path2 = p[-1]
            print(p)
            print(path2)
            results = utils.detect(path2)
            return Response(results, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)