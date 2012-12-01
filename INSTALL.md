Installation
============

This app is designed for easy deployment with Heroku so you can be up and
running with a functional app very quickly.

Deploy
------

First S3 setup:

1. Sign up for Amazon S3 - File storage for pennies a month
2. Create an Amazon S3 Bucket for file storage and add the following as a
   bucket policy. This will allow public reads from your bucket. NB: You will
   need to change `mybucketname` to the name of your bucket.

```
{
	"Version": "2008-10-17",
	"Statement": [
		{
			"Sid": "AllowPublicRead",
			"Effect": "Allow",
			"Principal": {
				"AWS": "*"
			},
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::mybucketname/*"
		}
	]
}
```

Second, Heroku setup and deployment:

3. Sign up for Heroku
4. Download and install the Heroku toolchain
5. Open Terminal and cd to the folder you put this app
6. Run the following commands, changing data as appropriate

```
heroku create
heroku config:add S3_KEY=mykey
heroku config:add S3_SECRET=mysecret
heroku config:add S3_BUCKET=mybucketname
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

