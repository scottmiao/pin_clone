pin_clone
=========

## Usage

### Initial

```bash
$ heroku login
$ heroku create pin-clone
$ heroku plugins:install https://github.com/ddollar/heroku-push
$ heroku push https://github.com/scottmiao/pin_clone.git
```

### Database

```bash
$ heroku addons:add heroku-postgresql:dev
-----> Adding heroku-postgresql:dev to some-app-name... done, v196 (free)
Attached as HEROKU_POSTGRESQL_COLOR
Database has been created and is available
$ heroku pg:promote HEROKU_POSTGRESQL_COLOR
```

> Don't forget to pip require psycopg2

