# Uon Alumni Project

## Railway deployment

This project is ready for Railway deployment using the existing `Procfile`.

### Required environment variables

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS=*`
- `DATABASE_URL`

### Recommended Railway setup

1. Create a new Railway project from this Git repository.
2. Add the PostgreSQL plugin or another database and copy the generated `DATABASE_URL`.
3. Add the environment variables above in Railway.
4. Deploy.

### Local setup

```bash
python -m pip install -r requirements.txt
cp .env.example .env
# update .env values
python manage.py migrate
python manage.py runserver
```

### Notes

- `Procfile` now uses `gunicorn main.wsgi --log-file -`.
- Settings are configured to read production values from environment variables.
- `.gitignore` excludes the local virtual environment, SQLite database, staticfiles, and environment files.
