from django.http import JsonResponse
from novel.serializers.all_book_serializer import BookCategorySerializer, BookSearchSerializer, BookInfoSerializer
from novel.models import BookCategory, BookInfo, BookContent
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def category_list(request):
    work_direction = request.GET.get('workDirection', 0)
    categories = BookCategory.objects.filter(work_direction=work_direction)
    serializer = BookCategorySerializer(categories, many=True)
    response_data = {
        "code": "00000",
        "message": "一切 ok",
        "data": serializer.data,
        "ok": True
    }
    return Response(response_data)


@api_view(['GET'])
def book_search(request):
    # 获取请求参数
    pageSize = int(request.GET.get('pageSize', 10))
    workDirection = int(request.GET.get('workDirection', 0))
    keyword = request.GET.get('keyword', '')
    categoryId = int(request.GET.get('categoryId', 0))
    isVip = int(request.GET.get('isVip', -1))
    bookStatus = int(request.GET.get('bookStatus', -1))
    wordCountMin = int(request.GET.get('wordCountMin', 0))
    wordCountMax = int(request.GET.get('wordCountMax', 0))
    updateTimeMin = request.GET.get('updateTimeMin', '')
    sort = request.GET.get('sort', '')
    pageNum = int(request.GET.get('pageNum', 1))

    # 构建查询条件
    filters = {}
    if workDirection != 0:
        filters['work_direction'] = workDirection
    if keyword:
        filters['book_name__icontains'] = keyword
    if categoryId != 0:
        filters['category_id'] = categoryId
    if isVip != -1:
        filters['is_vip'] = isVip
    if bookStatus != -1:
        filters['book_status'] = bookStatus
    if wordCountMin != 0:
        filters['word_count__gte'] = wordCountMin
    if wordCountMax != 0:
        filters['word_count__lte'] = wordCountMax
    if updateTimeMin:
        filters['last_chapter_update_time__gte'] = updateTimeMin

    # 排序
    if sort:
        sort_field = sort.strip('-')
        if sort.startswith('-'):
            sort_field = '-' + sort_field
        queryset = BookInfo.objects.filter(**filters).order_by(sort_field)
    else:
        queryset = BookInfo.objects.filter(**filters)

    # 分页
    total = queryset.count()
    start_index = (pageNum - 1) * pageSize
    end_index = start_index + pageSize
    queryset = queryset[start_index:end_index]

    # 构建响应数据
    books_list = []
    for book in queryset:
        book_data = {
            "id": book.id,
            "categoryId": book.category_id,
            "categoryName": book.category_name,
            "picUrl": book.pic_url,
            "bookName": book.book_name,
            "authorId": book.author_id,
            "authorName": book.author_name,
            "bookDesc": book.book_desc,
            "bookStatus": book.book_status,
            "visitCount": book.visit_count,
            "wordCount": book.word_count,
            "commentCount": book.comment_count,
            "firstChapterId": None,
            "lastChapterId": book.last_chapter_id,
            "lastChapterName": book.last_chapter_name,
            "updateTime": book.last_chapter_update_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }
        books_list.append(book_data)

    response_data = {
        "code": "00000",
        "message": "一切 ok",
        "data": {
            "pageNum": pageNum,
            "pageSize": pageSize,
            "total": total,
            "list": books_list,
            "pages": (total + pageSize - 1) // pageSize
        },
        "ok": True
    }

    return JsonResponse(response_data)


@api_view(['GET'])
def book_detail(request):
    # 获取请求参数
    bookId = int(request.GET.get('bookId', 0))

    try:
        # 查询小说信息
        book = BookContent.objects.get(chapter_id=bookId)
    except BookInfo.DoesNotExist:
        response_data = {
            "code": "404",
            "message": "Not Found",
            "data": [],
            "ok": False
        }
        return JsonResponse(response_data, status=404)

    # 构建响应数据
    book_data = {
        "id": book.id,
        "categoryId": book.category_id,
        "categoryName": book.category_name,
        "picUrl": book.pic_url,
        "bookName": book.book_name,
        "authorId": book.author_id,
        "authorName": book.author_name,
        "bookDesc": book.book_desc,
        "bookStatus": book.book_status,
        "visitCount": book.visit_count,
        "wordCount": book.word_count,
        "commentCount": book.comment_count,
        "firstChapterId": book.bookchapter_set.first().id if book.bookchapter_set.first() else None,
        "lastChapterId": book.last_chapter_id,
        "lastChapterName": book.last_chapter_name,
        "updateTime": book.last_chapter_update_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    }

    response_data = {
        "code": "00000",
        "message": "一切 ok",
        "data": [book_data],
        "ok": True
    }

    return JsonResponse(response_data)


class BookRecommendationListView(APIView):
    def get(self, request):
        book_id = request.GET.get('bookId')

        if not book_id:
            return Response({
                "code": "400",
                "message": "Missing bookId",
                "data": [],
                "ok": False
            }, status=status.HTTP_400_BAD_REQUEST)

        book_info = BookInfo.objects.filter(id=book_id).first()
        if not book_info:
            return Response({
                "code": "404",
                "message": "Book not found",
                "data": [],
                "ok": False
            }, status=status.HTTP_404_NOT_FOUND)

        recommended_books = BookInfo.objects.filter(category_id=book_info.category_id).exclude(id=book_id)[:10]
        serializer = BookInfoSerializer(recommended_books, many=True)

        response_data = {
            "code": "00000",
            "message": "Success",
            "data": serializer.data,
            "ok": True
        }
        return Response(response_data, status=status.HTTP_200_OK)


class BookInfoDetailView(APIView):
    def get(self, request,book_id):

        if not book_id:
            return Response({
                "code": "400",
                "message": "Missing bookId",
                "data": {},
                "ok": False
            }, status=status.HTTP_400_BAD_REQUEST)

        book_info = BookInfo.objects.filter(id=book_id).first()
        if not book_info:
            return Response({
                "code": "404",
                "message": "Book not found",
                "data": {},
                "ok": False
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = BookInfoSerializer(book_info)
        response_data = {
            "code": "00000",
            "message": "Success",
            "data": serializer.data,
            "ok": True
        }
        return Response(response_data, status=status.HTTP_200_OK)


class BookVisitView(APIView):
    def post(self, request):
        book_id = request.data.get('bookId')
        print(book_id)
        if not book_id:
            return Response({
                "code": "40001",
                "message": "Missing bookId",
                "data": None,
                "ok": False
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            book_info = BookInfo.objects.get(id=book_id)
            book_info.visit_count += 1
            book_info.save()
        except BookInfo.DoesNotExist:
            return Response({
                "code": "40401",
                "message": "Book not found",
                "data": None,
                "ok": False
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "code": "00000",
            "message": "一切 ok",
            "data": None,
            "ok": True
        }, status=status.HTTP_200_OK)