# Encyclopedia

The script generates a site with articles used in the encyclopedia at [DEVMAN.org](https://devman.org). The provided articles are written in the`md` format and so are converted into `html` one. The information about the articles (topics, paths) is contained in `config.json`. The  `templates` directory contains templates for the home page and for an article page, which are then rendered in `generator.py` with the package `jinja2`. The `bootstrap` directory contains the necessary `css` and `js` files for the templates.
After downloading the repo, install the dependencies:
```#! bash
$ pip install -r requirements.txt
```

Here is an example of how the result looks like at the [GitHub Pages](https://bulbule.github.io/19_site_generator/site/index.html).


# Usage
```#! bash
$ python generator.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
