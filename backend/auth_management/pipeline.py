def set_user_data(backend, strategy, details, response, user=None, *args, **kwargs):
    """
    SNS認証時にプロバイダから取得したデータをプロフィールに設定する。
    """
    if backend.name == "line":
        # ユーザー名を取得。取得できなかった場合はuserIdをユーザー名とする。
        username = response.get('displayName', response['userId'])
        # アイコン未設定の場合は空文字を設定する。
        icon_url = response.get('pictureUrl', '')
        
        user.username = username
        user.sns_icon_url = icon_url
        user.save()