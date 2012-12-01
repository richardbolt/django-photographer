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
otherwise you can see `requirements.txt` for a full list of dependencies.

Installation
------------

* Read [`INSTALL.md`](https://github.com/richardbolt/django-photographer/tree/master/INSTALL.md) for specific installation instructions.
* [Heroku documentation](https://devcenter.heroku.com/articles/quickstart) for general detail on Heroku.

Themes
------

The App is initially supplied with a default theme "plain".

[Compass](http://compass-style.org/) was used to develop the default theme.
I recommend installing it, creating a new theme based on the default, and
checking out the files in [`themes/plain/sass-src/`](https://github.com/richardbolt/django-photographer/tree/master/themes/plain/sass-src) for details on how it is
put together and how Compass and Sass will make your life easier developing
a unique look for your site.

* `_base.sass` contains the basics like site width, colors, and so forth.
* `screen.css` is the primary theme file styling all the elements.
* `forms.sass` handles the form styles.

The default theme use the following jQuery libraries:

* jQuery Horizontal Scroller: http://manos.malihu.gr/jquery-custom-content-scroller/
* jQuery Cycle Lite Plugin: http://malsup.com/jquery/cycle/lite/

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