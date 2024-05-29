from django.http import JsonResponse
from django.utils.decorators import method_decorator

from novel.models import BookInfo, NewsInfo, HomeFriendLink, HomeBook
from novel.serializers.home_serializers import NewsInfoSerializer, BookInfoSerializer, BookUpdateSerializer, \
    HomeFriendLinkSerializer, HomeBookDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


class LatestNewsList(APIView):
    def get(self, request, format=None):
        # 获取最新的新闻列表，这里假设按更新时间排序
        news_list = NewsInfo.objects.all().order_by('-update_time')
        serializer = NewsInfoSerializer(news_list, many=True)
        return Response({
            "code": "00000",
            "message": "Success",
            "data": serializer.data,
            "ok": True
        })


class HomeBooksDetailView(APIView):
    def get(self, request):
        # 获取 HomeBook 数据
        home_books = HomeBook.objects.all().order_by('sort')
        book_ids = [hb.book_id for hb in home_books]
        books = BookInfo.objects.filter(id__in=book_ids)
        book_map = {book.id: book for book in books}
        data = []
        for home_book in home_books:
            book_info = book_map.get(home_book.book_id)

            book_data = {
                'type': home_book.type,
                'bookId': str(home_book.book_id),
                'picUrl': book_info.pic_url,
                'bookName': book_info.book_name,
                'authorName': book_info.author_name,
                'bookDesc': book_info.book_desc,
            }
            data.append(book_data)
        # serializer = HomeBookDetailSerializer(home_books, many=True)
        return Response({
            "code": "00000",
            "message": "Success",
            "data": data,
            "ok": True
        })


class BookUpdatesView(APIView):
    def get(self, request, format=None):
        # 获取最近更新的小说列表，这里假设按最新章节更新时间排序
        books = BookInfo.objects.all().order_by('-last_chapter_update_time')[:10]  # 获取最新更新的10本书
        serializer = BookUpdateSerializer(books, many=True)
        return Response({
            "code": "00000",
            "message": "Success",
            "data": serializer.data,
            "ok": True
        })


class NewBooksView(APIView):
    def get(self, request, format=None):
        # 获取最新发布的小说列表，假设按 create_time 降序排序
        new_books = BookInfo.objects.all().order_by('-create_time')[:10]  # 获取最新的10本书
        serializer = BookUpdateSerializer(new_books, many=True)
        return Response({
            "code": "00000",
            "message": "Success",
            "data": serializer.data,
            "ok": True
        })


class BookVisitsView(APIView):
    def get(self, request, format=None):
        # 获取点击量最高的小说列表，假设按 visit_count 降序排序
        books = BookInfo.objects.all().order_by('-visit_count')[:10]  # 获取点击量最高的10本书
        serializer = BookUpdateSerializer(books, many=True)
        for item in serializer.data:
            item['id'] = str(item['id'])
        return Response({
            "code": "00000",
            "message": "Success",
            "data": serializer.data,
            "ok": True
        })


class BookUpdatesView(APIView):
    def get(self, request, format=None):
        # 获取最近更新的小说列表，这里假设按最新章节更新时间排序
        updated_books = BookInfo.objects.all().order_by('-last_chapter_update_time')[:10]  # 获取最新更新的10本书
        serializer = BookUpdateSerializer(updated_books, many=True)
        return Response({
            "code": "00000",
            "message": "Success",
            "data": serializer.data,
            "ok": True
        })

class FriendLinksView(APIView):
    def get(self, request, format=None):
        links = HomeFriendLink.objects.all().order_by('sort')  # 假设按 sort 排序
        serializer = HomeFriendLinkSerializer(links, many=True)
        return Response({
            "code": "00000",
            "message": "Success",
            "data": serializer.data,
            "ok": True
        })


def get_book_list(request):
    try:
        books = BookInfo.objects.all()
        data = []
        for book in books:
            book_data = {
                "type": book.work_direction,
                "bookId": book.id,
                "picUrl": book.pic_url,
                "bookName": book.book_name,
                "authorName": book.author_name,
                "bookDesc": book.book_desc
            }
            data.append(book_data)
        response_data = {
            "code": "00000",
            "message": "Success",
            "data": data,
            "ok": True
        }
        return JsonResponse(response_data)
    except Exception as e:
        response_data = {
            "code": "500",
            "message": str(e),
            "data": [],
            "ok": False
        }
        return JsonResponse(response_data)
