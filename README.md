<div>
  <h1 align="center">very-store</h1>
</div>

## Development

Is recommended to use a virtual environment for Python development.
Install [pyenv](https://github.com/pyenv/pyenv) to use multiple Python versions
and [pipenv](https://github.com/pypa/pipenv) to manage multiple virtual
environments

Install Python version 3.10.0 (specified in the `.python-version` file) using
`pyenv install 3.10.0`. Then install dependencies using _pipenv_ so a virtual
environment gets created for this project and holds dependencies as well.

Execute `pipenv install`, which will install dependencies listed in the _Pipfile_
TOML file, all scoped in a virtual environment for this project.

Finally open a _Pipenv_ shell to run further commands against the virtual
environment.

```bash
pipenv shell

((very-store) ) ➜  very-store git:(main)
```

> Is recommended to run further commands through the _Pipenv_ shell.

With all set you must run [database migrations](#database-migrations) and then
execute the Django server using `python manage.py runserver`.

### Database Migrations

Run SQL database migrations by running:

```bash
python manage.py migrate
```

### Code style

Run Black against the codebase by running:

```bash
python -m black ./*.py
```

You may see an output similar to this:

```
reformatted core/asgi.py
reformatted core/wsgi.py
reformatted core/urls.py
reformatted store/apps.py
reformatted manage.py
reformatted store/models.py
reformatted core/settings.py
All done! ✨ 🍰 ✨
7 files reformatted, 6 files left unchanged.
```

### Pyright Config

If you are using Pyright make sure you create a config file like the
following with the contents:

```js
// pyrightconfig.json
{
  "venvPath": "<Virtual Environments Directory Path>",
  "venv": "<Virtual Environment Directory Name>",
}
```

### Superuser for Development

When working on development environment is useful to have a superuser
to manage the application contentwise.

Django let's you create a super user by running the following command:

```bash
python manage.py createsuperuser
```

Fill the prompts with the desired data and then run open the server on
http://localhost:8000/admin to login with the recently created superuser.
