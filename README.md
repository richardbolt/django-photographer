Django App for photographers
============================

A Django app that has integrates a configured
[FeinCMS](http://www.feincms.org/)
content management system, a blog
([ElephantBlog](https://github.com/feincms/feincms-elephantblog)), and
provides a clean way to get a portfolio website and blog up and running
very quickly with [Heroku](http://www.heroku.com/) and
[Amazon S3](http://aws.amazon.com/s3/).

The app is designed to be used standalone with minimal programming knowledge
in that you can download it, push it to Heroku, and have a functional site
in minutes complete with placeholder pages ready for your content (mainly
images for portfolio pages).

The app can also be used as part of a custom app if you want to add more
features and apps to the base.


Dependencies
------------

If you install with Heroku, dependencies will be taken care of for you,
otherwise you can see `requirements.txt` for a full list of dependencies.

Installation
------------

* Read [`INSTALL.md`](https://github.com/richardbolt/django-photographer/tree/master/INSTALL.md) for specific installation instructions.
* [Heroku documentation](https://devcenter.heroku.com/articles/quickstart) for general detail on Heroku.

Themes
------

The App is initially supplied with a default theme "plain". The theme assets
are places in the `photographer/static/<themename>/` folder. The .sass files
used to develop the default theme styles are in the `themes` folder in the
root of the project.

[Compass](http://compass-style.org/) was used to develop the default theme css.
I recommend installing it, creating a new theme based on the default, and
checking out the files in [`themes/plain/sass-src/`](https://github.com/richardbolt/django-photographer/tree/master/themes/plain/sass-src) for details on how it is
put together and how Compass and Sass will make your life easier developing
a unique look for your site.

* `_base.sass` contains the basics like site width, colors, and so forth.
* `screen.css` is the primary theme file styling all the elements.
* `forms.sass` handles the form styles.

The default theme makes use of:
-------------------------------

**Icons**

Icons (currently only the home icon in the admin) are from the Iconic set:
http://somerandomdude.com/work/iconic/

**The following jQuery libraries**

* jQuery Horizontal Scroller: http://manos.malihu.gr/jquery-custom-content-scroller/
* jQuery Cycle Lite Plugin: http://malsup.com/jquery/cycle/lite/

There is a `templates` folder within the theme folder. This `templates` folder
is the first place searched for templates when the template machinery is
compiling the pages. What this means in practice is you can override any
template by placing it in that folder inside your theme. As an example there
is a `_head.html` file in the default `plain` theme folder.

License
-------

```
Copyright (c) 2012, Richard Bolt and individual contributors.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* The names of individual contributors may not be used to endorse or promote
  products derived from this software without specific prior written
  permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```