from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from novel.models import BookChapter,BookContent
from novel.serializers.chapter_serializer import ChapterSerializer

class LastChapterView(APIView):
    def get(self, request):
        book_id = request.GET.get('bookId')

        if not book_id:
            return Response({
                "code": "400",
                "message": "Missing bookId",
                "data": {
                    "chapterInfo": {},
                    "chapterTotal": 0,
                    "contentSummary": ""
                },
                "ok": False
            }, status=status.HTTP_400_BAD_REQUEST)

        last_chapter = BookChapter.objects.filter(book_id=book_id).order_by('-chapter_num').first()
        book_content = BookContent.objects.filter(chapter_id=last_chapter.id).first()
        if not last_chapter:
            return Response({
                "code": "404",
                "message": "No chapters found",
                "data": {
                    "chapterInfo": {},
                    "chapterTotal": 0,
                    "contentSummary": ""
                },
                "ok": False
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = ChapterSerializer(last_chapter)
        total_chapters = BookChapter.objects.filter(book_id=book_id).count()

        response_data = {
            "code": "00000",
            "message": "Success",
            "data": {
                "chapterInfo": serializer.data,
                "chapterTotal": total_chapters,
                "contentSummary": book_content.content[:35]
            },
            "ok": True
        }
        return Response(response_data, status=status.HTTP_200_OK)
