from django.contrib import admin
from .models import Comment  # 导入模型


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created')
    search_fields = ('author', 'content')
    list_filter = ('created', )


# 注册模型到 Django 管理后台
admin.site.register(Comment, CommentAdmin)
