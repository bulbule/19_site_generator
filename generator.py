import json
import os

from jinja2 import Environment, FileSystemLoader
import markdown


CONFIG = 'config.json'
TEMPLATES_PATH = 'templates'
ARTICLES_PATH = 'articles'
SITE_PATH = 'site'


def load_json(file_path):
    with open(file_path, encoding='utf-8') as json_file:
        return json.loads(json_file.read())


def load_md_file(file_path):
    with open(file_path, encoding='utf-8') as md_file:
        return md_file.read()


def load_jinja2_env():
    return Environment(loader=FileSystemLoader(TEMPLATES_PATH),
                       trim_blocks=True,
                       lstrip_blocks=True,)


def save_into_html(rendered_template, output_file):
    with open(output_file, 'w') as file:
        file.write(rendered_template)


def convert_to_html(md_file):
    return markdown.markdown(md_file,
                             extensions=['codehilite'])


def check_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def create_dir_for_article(article_path):
    article_dir = '{}/{}'.format(SITE_PATH, article_path.split('/')[1])
    check_dir(article_dir)


def get_html_article(article, article_template):
    article_path = '{}/{}'.format(ARTICLES_PATH, article['source'])
    html_content = convert_to_html(load_md_file(article_path))
    rendered_template = article_template.render(content=html_content,
                                                title=article['title'])
    create_dir_for_article(article_path)
    save_into_html(rendered_template,
                   '{}/{}'.format(SITE_PATH,
                                  article['source'].replace('md', 'html')))


def get_html_articles(config_json, article_template):
    for article in config_json['articles']:
        get_html_article(article, article_template)


if __name__ == '__main__':
    config_json = load_json(CONFIG)
    env = load_jinja2_env()
    main_template = env.get_template('template_main.html')
    save_into_html(
        main_template.render(topics=config_json['topics'],
                             articles=config_json['articles']),
        '{}/index.html'.format(SITE_PATH)
    )

    article_template = env.get_template('template_article.html')
    get_html_articles(config_json, article_template)
