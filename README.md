Django App for photographers
============================

A Django app that has integrates a configured
[FeinCMS](http://www.feincms.org/)
content management system, a blog
([ElephantBlog](https://github.com/feincms/feincms-elephantblog)), and
provides a clean way to get a portfolio website and blog up and running
very quickly with [Heroku](http://www.heroku.com/).


Dependencies
------------

If you install with Heroku, dependencies will be taken care of for you,
otherwise you can see requirements.txt for a full list of dependencies.

Installation
------------

* Deploy with Heroku - see the [Heroku documentation](https://devcenter.heroku.com/articles/quickstart) for more detail.
* More detail to come.

Themes
------

The App is initially supplied with a default theme "plain".

[Compass](http://compass-style.org/) was used to develop the default theme.
I recommend installing it, creating a new theme based on the default, and
checking out the files in [themes/plain/sass-src/](https://github.com/richardbolt/django-photographer/tree/master/themes/plain/sass-src) for details on how it is
put together and how Compass and Sass will make your life easier developing
a unique look for your site.

* _base.sass contains the basics like site width, colors, and so forth.
* screen.css is the primary theme file styling all the elements.
* forms.sass handles the form styles.
