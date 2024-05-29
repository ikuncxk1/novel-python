from rest_framework import serializers
from novel.models import BookChapter


class ChapterSerializer(serializers.ModelSerializer):
    bookId = serializers.IntegerField(source='book_id')
    chapterNum = serializers.IntegerField(source='chapter_num')
    chapterName = serializers.CharField(source='chapter_name')
    chapterWordCount = serializers.IntegerField(source='word_count')
    chapterUpdateTime = serializers.DateTimeField(source='update_time')
    isVip = serializers.BooleanField(source='is_vip')

    class Meta:
        model = BookChapter
        fields = ['id', 'bookId', 'chapterNum', 'chapterName', 'chapterWordCount', 'chapterUpdateTime', 'isVip']

