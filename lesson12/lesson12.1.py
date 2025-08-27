import re
import codecs
import html as html_lib


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt', drop_empty: bool = False) -> None:
    """
    Читає HTML-файл, прибирає теги і пише очищений текст у result_file.
    drop_empty=True — додатково прибирає порожні рядки.
    """
    with codecs.open(html_file, 'r', 'utf-8') as f:
        html = f.read()

    # прибрати <script>/<style> разом із вмістом
    html = re.sub(r'(?is)<(script|style).*?>.*?</\1>', '', html)
    # прибрати всі теги
    text = re.sub(r'(?s)<[^>]+>', '', html)
    # розшифрувати HTML-ентіті (&nbsp;, &amp; тощо)
    text = html_lib.unescape(text)

    lines = [line.strip() for line in text.splitlines()]
    if drop_empty:
        lines = [line for line in lines if line]

    with codecs.open(result_file, 'w', 'utf-8') as out:
        out.write('\n'.join(lines))

delete_html_tags('draft.html', 'cleaned.txt', drop_empty=True)
print(open('cleaned.txt', encoding='utf-8').read())
