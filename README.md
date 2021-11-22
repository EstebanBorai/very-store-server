<div>
  <h1 align="center">very-store</h1>
</div>

## Code format

Black is used to for fixing codebase format, install Black using
pip as follows:

```bash
python -m pip install --user black
```

Then run Black against the codebase by running:

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
