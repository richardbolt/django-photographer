Installation
============

This app is designed for easy deployment with Heroku so you can be up and
running with a functional app very quickly.

Deploy on Heroku
----------------

1. Sign up for Heroku
2. Download and install the Heroku toolchain
3. Open Terminal and cd to the folder you put this app
4. Run the following commands, changing data as appropriate

```
heroku create
heroku config:add DJANGO_SECRET_KEY='completely-random-secret-key-here'
heroku config:add RB_SITE_TITLE='My Site Title'
heroku config:add BLOG_TITLE=RB_SITE_TITLE
heroku config:add BLOG_DESCRIPTION='My blog description'
heroku config:add ADMIN_NAME=RB_SITE_TITLE
heroku config:add ADMIN_EMAIL=me@mydomain.com
git push heroku master
heroku run ./manage.py syncdb
heroku run ./manage.py loaddata photographer/fixtures/skeleton.json
```

You should now be up and running. To visit your site type `heroku open`.


Optional configuration parameters
---------------------------------

Add Facebook and Twitter handles:

```
heroku config:add RB_FACEBOOK=richardbolt
heroku config:add RB_TWITTER_HANDLE=richardbolt
```

Use debug mode (if you experience problems)

```
heroku config:add DJANGO_DEBUG=True
```

Turn off debug mode when all is well

```
heroku config:remove DJANGO_DEBUG
```

DNS
---

You will need to edit your DNS settings so that you can use your url with
your new website. Details here: https://devcenter.heroku.com/articles/custom-domains


Notes
-----

The default theme use the following js libraries:

* jQuery
* jQuery Horizontal Scroller: http://manos.malihu.gr/jquery-custom-content-scroller/
