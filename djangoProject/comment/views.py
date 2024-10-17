from django.http import JsonResponse
from .models import Comment
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods
from datetime import datetime
import pytz


def time_switching(raw_time):
    """转换时间时区
        Args:
            raw_time:修改前时间字符串
        Returns:
            output:修改后时间字符串
        """
    if isinstance(raw_time, datetime):
        utc_time = raw_time.replace(tzinfo=pytz.utc)
    else:
        utc_time = datetime.strptime(raw_time, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc)
    later_time_zone = pytz.timezone('Asia/Shanghai')
    later_time = utc_time.astimezone(later_time_zone)
    output = str(later_time.strftime('%Y-%m-%d %H:%M:%S'))
    return output


def comments_get(request):
    # noinspection PyUnresolvedReferences
    """按照页码获取评论内容
            Args:
                request: GET
                page(int): 页码
            Returns:
                comments(Json): 评论列表
                page(int): 页码
            """
    page = int(request.GET.get('page', 1))  # 前端传递的页码，默认为第 1 页
    # 每页显示 10 条数据
    page_size = 10
    start = (page - 1) * page_size
    end = start + page_size

    # 获取前 10 条或分页后的数据
    comments = Comment.objects.all().order_by('-created')[start:end]

    # 将数据转换为可返回的 JSON 格式
    comment_list = [
        {
            "id": comment.id,
            "author": comment.author,
            "content": comment.content,
            "created": time_switching(comment.created),
        }
        for comment in comments
    ]

    return JsonResponse({
        "comments": comment_list,
        "page": page
    })


def comment_add(request):
    # noinspection PyUnresolvedReferences
    """添加评论
            Args:
                request: POST
                author(str)
                content(str)
            Returns:
                message:评论添加成功
            Raises:
                401:作者和内容不能为空
                402:内容不能超过150个字符
                403:目前没出现
                405:请求方法错误
            """
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')

        # 检查数据是否有效
        if not author or not content:
            return JsonResponse({"error": "作者和内容不能为空"}, status=401)

        if len(content) > 150:
            return JsonResponse({"error": "内容不能超过150个字符"}, status=402)

        # 创建评论并保存到数据库
        comment = Comment(author=author, content=content)
        try:
            comment.full_clean()  # 验证模型字段
            comment.save()
            return JsonResponse({"message": "评论添加成功"}, status=200)
        except ValidationError as e:
            return JsonResponse({"error": e.message_dict}, status=403)

    return JsonResponse({"error": "请求方法错误"}, status=405)


@require_http_methods(["DELETE"])
def comment_delete(request):
    # noinspection PyUnresolvedReferences
    """
        Args:
            request: DELETE
            comment_id: 评论id
        Returns:
            message: 评论已成功删除
            status：204
        Raises:
            404：评论不存在
        """
    try:
        comment_id = request.GET.get('id')
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return JsonResponse({"message": "评论已成功删除"}, status=204)
    except Comment.DoesNotExist:
        return JsonResponse({"error": "评论不存在"}, status=404)
