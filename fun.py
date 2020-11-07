import keyword

def keyword_check(user_str):
    print(f'Keyword = {keyword.iskeyword(user_str)}')