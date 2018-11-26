# docker-django

A simple spelling application as a demonstration docker-compose
project with both Postgres and Django running in different Docker
containers.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

First, clone or copy the project locally.  Make sure you have
installed Docker and Docker Compose.  Then, start the servers in one
terminal with the following

```
docker-compose up --build
```

Once running, you should be able to visit the `spelling` URL and look
up incorrectly spelled words.

## Usage

Before using this for the first time, you will need to load a dictionary of words.  For English, I recommend the following link:
[english-words](https://github.com/dwyl/english-words)

To load the words (which takes about an hour on a Macbook Pro), use a
different terminal window and find the name of the docker instance
containing the web server (Django).

```
docker ps
```

Look for the result with the text `web_1` in the name.  Copy its entire name and execute the following commands with this name:

```
docker exec -it docker-django_web_1_aabbcc python manage.py makemigrations
docker exec -it docker-django_web_1_aabbcc python manage.py migrate
docker exec -it docker-django_web_1_aabbcc python manage.py shell
```

The last command will enter you into a shell where you can load the words file.  If you have loaded `words_alpha.txt` into the same root directory as the `docker-django` project, then you can execute the following commands in the shell:

```
from spelling.make_ngrams import load_words
load_words('words_alpha.txt')
```

## Support

No support for now, but feel free to leave a comment on the page.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/fraction/readme-boilerplate/compare/).
