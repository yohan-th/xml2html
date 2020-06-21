import os
import sys

def read_file(f):
    if not os.path.isfile(f):
        print(f'{f} file or path incorrect. EXIT')
        sys.exit(1)
    else:
        with open(f, 'r') as fl:
            data = fl.read()
    return(data)

def add_new_article(html):
    art_template = '''
    <article>
        <details class="entry">
        <summary>
            <header class="entry-header">
                <h1 class="entry-title"><a class="entry-link" href="PY_A_HREF" title="PY_A_TITLE">PY_A_TITLE</a></h1>
                <p class="entry-date"><time>PY_A_TIME</time></p>
            </header>
        </summary>
        <!DOCTYPE html>
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head><link rel="stylesheet" href="./assets/entry-content.css"/></head>
            <body>
                PY_A_BODY
            </body>
        </html>
        </details>
    </article>'''
    html = html.replace('PY_ARTICLE', art_template+'PY_ARTICLE')
    return html
