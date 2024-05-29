from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from novel.models import UserComment
from novel.serializers.comment_serizlizer import UserCommentSerializer


class NewestCommentsView(APIView):
    def get(self, request):
        book_id = request.GET.get('bookId')
        if not book_id:
            return Response({
                "code": "400",
                "message": "Missing bookId",
                "data": {
                    "commentTotal": 0,
                    "comments": []
                },
                "ok": False
            }, status=status.HTTP_400_BAD_REQUEST)

        comments = UserComment.objects.filter(book_id=book_id).order_by('-create_time')
        serializer = UserCommentSerializer(comments, many=True)

        response_data = {
            "code": "00000",
            "message": "Success",
            "data": {
                "commentTotal": comments.count(),
                "comments": serializer.data
            },
            "ok": True
        }
        return Response(response_data, status=status.HTTP_200_OK)
