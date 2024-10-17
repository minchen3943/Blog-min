from django.http import JsonResponse
from .models import Comment
from django.core.exceptions import ValidationError


def comment_add(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')

        # 检查数据是否有效
        if not author or not content:
            return JsonResponse({"error": "作者和内容不能为空"}, status=400)

        if len(content) > 150:
            return JsonResponse({"error": "内容不能超过150个字符"}, status=400)

        # 创建评论并保存到数据库
        comment = Comment(author=author, content=content)
        try:
            comment.full_clean()  # 验证模型字段
            comment.save()
            return JsonResponse({"message": "评论添加成功", "comment": {
                "author": comment.author,
                "content": comment.content,
                "created": comment.created
            }})
        except ValidationError as e:
            return JsonResponse({"error": e.message_dict}, status=400)

    return JsonResponse({"error": "请求方法错误"}, status=405)

