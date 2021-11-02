from functools import wraps

from .models import User
from utils.http import make_json_response


def _login_required(error='未登录'):
    # 判断是否登录的decorator
    def is_login(request):
        if request.method != 'POST':
            return False
        username = request.POST.get('username', '')
        token = request.POST.get('token', '')
        print(f'username={username} token={token}')
        try:
            user = User.objects.get(username=username)
        except:
            print('用户不存在')
            return False
        if not user.check_token(token) or not user.tokens.filter(token=token):
            print('token无效')
            return False
        print('已登录')
        if hasattr(request, 'user'):
            request.user = user
        return True

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if is_login(request):
                return view_func(request, *args, **kwargs)
            return make_json_response(code=401, error=error)
        return _wrapped_view

    return decorator

login_required = _login_required()