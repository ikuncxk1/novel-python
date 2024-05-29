from rest_framework import serializers
from novel.models import BookCategory, BookInfo


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('id', 'name')


class BookSearchSerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source='category_name')
    authorName = serializers.CharField(source='author_name')
    firstChapterId = serializers.SerializerMethodField()
    lastChapterId = serializers.SerializerMethodField()
    lastChapterName = serializers.CharField(source='last_chapter_name')
    updateTime = serializers.DateTimeField(source='last_chapter_update_time')

    class Meta:
        model = BookInfo
        fields = (
            'id', 'category_id', 'category_name', 'pic_url', 'book_name', 'author_id', 'author_name',
            'book_desc', 'book_status', 'visit_count', 'word_count', 'comment_count'
            , 'last_chapter_id', 'last_chapter_name', 'update_time'
        )

    def get_firstChapterId(self, obj):
        return obj.bookchapter_set.first().id if obj.bookchapter_set.first() else None

    def get_lastChapterId(self, obj):
        return obj.last_chapter_id


class BookInfoSerializer(serializers.ModelSerializer):
    categoryId = serializers.IntegerField(source='category_id')
    categoryName = serializers.CharField(source='category_name')
    picUrl = serializers.CharField(source='pic_url')
    bookName = serializers.CharField(source='book_name')
    authorId = serializers.IntegerField(source='author_id')
    authorName = serializers.CharField(source='author_name')
    bookDesc = serializers.CharField(source='book_desc')
    bookStatus = serializers.IntegerField(source='book_status')
    visitCount = serializers.IntegerField(source='visit_count')
    wordCount = serializers.IntegerField(source='word_count')
    commentCount = serializers.IntegerField(source='comment_count')
    lastChapterId = serializers.IntegerField(source='last_chapter_id')
    lastChapterName = serializers.CharField(source='last_chapter_name')
    updateTime = serializers.DateTimeField(source='update_time')

    class Meta:
        model = BookInfo
        fields = [
            'id', 'categoryId', 'categoryName', 'picUrl', 'bookName',
            'authorId', 'authorName', 'bookDesc', 'bookStatus', 'visitCount',
            'wordCount', 'commentCount', 'lastChapterId', 'lastChapterName', 'updateTime'
        ]