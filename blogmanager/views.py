from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Blog
from .serializers import BlogSerializer
from django.utils import timezone
from Blogs import settings
import logging
    
logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('django')


class BlogManaging(APIView):


    def post(self, request):
        data = request.data
        logger.error('Entered method for saving blog')
        try:
            serializerd_data = BlogSerializer(data=data)
            if serializerd_data.is_valid():
                serializerd_data.save()
                response_data = {
                            'uri': request._request.path,
                            'created':True,
                            'responsecode':201,
                            'description':'blog got saved successfully'}
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data = {'uri':request._request.path,
                                   'description':'Invalid data',
                                   'responsecode':400}
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception, e:
            logger.error(e)
            logger.error('Got exception. Returning Internal server error')
            response_data = {'uri':request._request.path,
                               'description':'Internal server error',
                               'detail':'Internal server error',
                               'responsecode':500}
            return Response(
                response_data,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):

        blog_id = request.GET.get('blog_id')
        try:
            blog = Blog.objects.get(pk=blog_id)
            serialized_data = BlogSerializer(blog).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            response_data = {'uri':request._request.path,
                               'description':'No such Blog id',
                               'responsecode':400}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception, e:
            logger.error(e)
            logger.error('Got exception. Returning Internal server error')
            response_data = {'uri':request._request.path,
                               'description':'Internal server error',
                               'detail':'Internal server error',
                               'responsecode':500}
            return Response(
                response_data,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            blog_id = request.GET.get('blog_id')
            blog_obj = Blog.objects.get(pk=blog_id)
            if request.data.has_key('name'):
                blog_obj.name = request.data['name']
            if request.data.has_key('title'):
                blog_obj.title = request.data['title']
            if request.data.has_key('description'):
                blog_obj.description = request.data['description']
            blog_obj.update_at = timezone.now()
            blog_obj.save()
            response_data = {
                            'uri': request._request.path,
                            'updated':True,
                            'responsecode':200,
                            'description':'blog got updated successfully'}
            return Response(response_data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            response_data = {'uri':request._request.path,
                               'description':'No such Blog id',
                               'responsecode':400}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception, e:
            logger.error(e)
            logger.error('Got exception. Returning Internal server error')
            response_data = {'uri':request._request.path,
                               'description':'Internal server error',
                               'detail':'Internal server error',
                               'responsecode':500}
            return Response(
                response_data,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            blog_id = request.GET.get('blog_id')
            blog_obj = Blog.objects.get(pk=blog_id)
            blog_obj.delete()
            response_data = {
                            'uri': request._request.path,
                            'responsecode':200,
                            'description':'blog got deleted successfully'}
            return Response(response_data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            response_data = {'uri':request._request.path,
                               'description':'No such Blog id',
                               'responsecode':400}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception, e:
            logger.error(e)
            logger.error('Got exception. Returning Internal server error')
            response_data = {'uri':request._request.path,
                               'description':'Internal server error',
                               'detail':'Internal server error',
                               'responsecode':500}
            return Response(
                response_data,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)



