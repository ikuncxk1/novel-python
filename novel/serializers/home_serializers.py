from rest_framework import serializers
from novel.models import NewsInfo, NewsContent, BookInfo, HomeFriendLink, HomeBook


class NewsInfoSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    updateTime = serializers.DateTimeField(source='update_time')

    class Meta:
        model = NewsInfo
        fields = ('id', 'category_id', 'category_name', 'source_name', 'title', 'updateTime', 'content')

    def get_content(self, obj):
        # 假设每个 NewsInfo 只有一个对应的 NewsContent
        content = NewsContent.objects.filter(news_id=obj.id).first()
        return content.content if content else None

# 首页小说推荐查询接口
class BookInfoSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    bookId = serializers.IntegerField(source='id')
    picUrl = serializers.CharField(source='pic_url')
    bookName = serializers.CharField(source='book_name')
    authorName = serializers.CharField(source='author_name')
    bookDesc = serializers.CharField(source='book_desc')

    class Meta:
        model = BookInfo
        fields = ('type', 'bookId', 'picUrl', 'bookName', 'authorName', 'bookDesc')

    def get_type(self, obj):
        # 这里可以根据你的需求调整类型的确定逻辑
        return 0  # 示例中始终返回 0


class HomeBookDetailSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField()  # 获取 HomeBook 中的 type
    bookId = serializers.IntegerField(source='book.id')
    picUrl = serializers.CharField(source='book.pic_url')
    bookName = serializers.CharField(source='book.book_name')
    authorName = serializers.CharField(source='book.author_name')
    bookDesc = serializers.CharField(source='book.book_desc')

    class Meta:
        model = HomeBook
        fields = ['type', 'bookId', 'picUrl', 'bookName', 'authorName', 'bookDesc']

    def __init__(self, *args, **kwargs):
        # 初始化时预先加载相关的 BookInfo 数据
        super().__init__(*args, **kwargs)
        self.books = {book.id: book for book in BookInfo.objects.filter(id__in=[hb.book_id for hb in self.instance])}

    def to_representation(self, instance):
        # 自定义表示以整合来自 BookInfo 的数据
        representation = super().to_representation(instance)
        book = self.books.get(instance.book_id)
        if book:
            representation.update({
                'picUrl': book.pic_url,
                'bookName': book.book_name,
                'authorName': book.author_name,
                'bookDesc': book.book_desc
            })
        return representation

# 小说更新榜序列器
class BookUpdateSerializer(serializers.ModelSerializer):
    categoryId = serializers.CharField(source='category_id')
    categoryName = serializers.CharField(source='category_name')
    picUrl = serializers.CharField(source='pic_url')
    bookName = serializers.CharField(source='book_name')
    authorName = serializers.CharField(source='author_name')
    bookDesc = serializers.CharField(source='book_desc')
    wordCount = serializers.IntegerField(source='word_count')
    lastChapterName = serializers.CharField(source='last_chapter_name')
    lastChapterUpdateTime = serializers.DateTimeField(source='last_chapter_update_time', format="%Y-%m-%dT%H:%M:%S.%fZ")

    class Meta:
        model = BookInfo
        fields = ('id', 'categoryId', 'categoryName', 'picUrl', 'bookName', 'authorName', 'bookDesc', 'wordCount', 'lastChapterName', 'lastChapterUpdateTime')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category_id'] = str(instance.category_id)  # 将 ID 转换为字符串
        return representation


class HomeFriendLinkSerializer(serializers.ModelSerializer):
    linkName = serializers.CharField(source='link_name')
    linkUrl = serializers.CharField(source='link_url')

    class Meta:
        model = HomeFriendLink
        fields = ('linkName', 'linkUrl')