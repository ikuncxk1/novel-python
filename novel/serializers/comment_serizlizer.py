from rest_framework import serializers
from novel.models import UserComment


class UserCommentSerializer(serializers.ModelSerializer):
    commentUser = serializers.SerializerMethodField()
    commentUserPhoto = serializers.SerializerMethodField()

    class Meta:
        model = UserComment
        fields = ['id', 'comment_content', 'user_id', 'create_time', 'commentUser', 'commentUserPhoto']

    def get_commentUser(self, obj):
        return obj.user_id  # 这里你可以根据具体需求修改，假设User模型中有username字段

    def get_commentUserPhoto(self, obj):
        return ""  # 假设没有用户头像数据
