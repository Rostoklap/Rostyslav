def popular_words (text: str, words: list[str]) -> dict[str, int]:
    tokens = text.lower().split()
    return {w: tokens.count(w) for w in words}


assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
