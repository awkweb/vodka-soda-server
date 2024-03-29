# vodka-soda-server

> Casual without compromise

## Set Up Local Dev Environment

Install tools and dependencies (via [homebrew](https://brew.sh/)):

```bash
> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
> brew tap homebrew/bundle
> brew bundle
```

Next, create a local Postgres database:

1. Open `postgres.app` (just installed via `brew`)
2. Open `postico.app`
3. Create a database through `positico`

Add environment variables:

```bash
# DJANGO APP KEYS

export DJ_ENV=dev
export DJ_DB_NAME=vodka-soda # database you just created
export DJ_DB_USER=tom # this is likely the user you use to login to your computer
export DJ_DB_PASSWORD=root
export DJ_DB_HOST=docker.for.mac.localhost # special docker set up
export DJ_DB_PORT=5432
export DJ_SECRET_KEY=+cg9iso$a55f3ay&)pdg3k&=lq_c*55j7oyuib=a(pi#2$oj^0
export DJ_SOCIAL_AUTH_FACEBOOK_KEY=234928371610299
export DJ_SOCIAL_AUTH_FACEBOOK_SECRET=3731939d837s7b1b0b772a64c7570edb

# FLASK APP KEYS

export FLASK_APP=app.py

# LETS ENCRYPT CERTIFICATE PATHS

export SSL_CERTIFICATE=/etc/nginx/certs/local/vodkasoda.crt
export SSL_CERTIFICATE_KEY=/etc/nginx/certs/local/vodkasoda.key
```

Update `/etc/hosts` by adding:

```bash
0.0.0.0 vodkasoda.local api.vodkasoda.local www.vodkasoda.local
```

Snag the repo, start Docker, and build the containers:

```bash
> git clone https://github.com/tmm/vodka-soda-server.git
> cd vodka-soda-server
> docker-compose build
```

Apply database migrations, create superuser, and generate static files (for admin console, etc.):

```bash
> docker-compose run api python manage.py makemigrations
> docker-compose run api python manage.py migrate
> docker-compose run api python manage.py collectstatic
```

Generate a local wildcard cert by running `bash scripts/generate-wildcard-cert.sh` and entering `vodkasoda.local` for root domain. Add the generated `certs` dir to `nginx/certs`. If everything worked as planned, you should be able to `docker-compose up` and access the admin app.

```bash
> docker-compose up -d
> docker-compose ps
CONTAINER ID        IMAGE                    COMMAND                  CREATED            STATUS            PORTS                NAMES
13cf068eefeb        vodkasodaserver_nginx    "nginx -g 'daemon of…"   1 minute ago       Up 1 minute       0.0.0.0:80->80/tcp   nginx
18f7d8df9ef9        vodkasodaserver_web      "uwsgi --ini uwsgi.i…"   1 minute ago       Up 1 minute       5000/tcp             web
f2bc789461bf        vodkasodaserver_api      "uwsgi --ini uwsgi.i…"   1 minute ago       Up 1 minute       8000/tcp             api
```

Go to the [admin site](https://api.vodkasoda/admin/oauth2_provider/application/add/) to create a new `Application` for the API to connect to.

## Creating/Updating DB Models

Whenever you make changes to a model, the database needs to be kept in sync.

```bash
> docker-compose run api python manage.py makemigrations
> docker-compose run api python manage.py migrate
```

See [Django Migrations Worflow](https://docs.djangoproject.com/en/2.0/topics/migrations/#workflow) for more info.

## Set Up Production Environment

1) Create RDS Postgres instance

2) Add production environment variables to `.env`:

```bash
# DJANGO APP KEYS

export DJ_ENV=prod
export DJ_DB_NAME=something
export DJ_DB_USER=root
export DJ_DB_PASSWORD=zsRqfjJdDVAxhUewsqnTCxlslr
export DJ_DB_HOST=something.cxsbe1vrwmpg.us-east-1.rds.amazonaws.com
export DJ_DB_PORT=5432
export DJ_SECRET_KEY=+cg9iso$a55f3ay&)pdg3k&=lq_c*55j7oyuib=a(pi#2$oj^0
export DJ_SOCIAL_AUTH_FACEBOOK_KEY=234928371610299
export DJ_SOCIAL_AUTH_FACEBOOK_SECRET=3731939d837s7b1b0b772a64c7570edb

# FLASK APP KEYS

export FLASK_APP=app.py

# AWS IAM ACCESS KEYS

export AWS_ACCESS_KEY_ID=AKIATEMMAIEPJOZC74GP
export AWS_SECRET_ACCESS_KEY=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

# LETS ENCRYPT CERTIFICATE PATHS

export SSL_CERTIFICATE=/etc/nginx/certs/letsencrypt/name.crt
export SSL_CERTIFICATE_KEY=/etc/nginx/certs/letsencrypt/name.key
```

3) Build, tag, and push Docker images to [Amazon Elastic Container Registry](https://console.aws.amazon.com/ecs/home?region=us-east-1#/repositories)

4) Update `image` paths in `aws-compose.yml` (from now on you may use `bash scripts/push-aws-ecr.sh` to build, tag, and push all images)

5) [Create a new keypair on EC2](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:sort=keyName)

6) Add RDS's `vpc` (`--vpc vpc_id`) and `subnets` (`--subnets subnet_1,subnet_2`) to `scripts/setup-aws-ecs.sh`

7) [Configure `ecs-cli`](https://docker-curriculum.com/#aws-ecs) with cluster info by running `bash scripts/setup-aws-ecs.sh`

8) Run deploy script `bash scripts/deploy-aws-ecs.sh` ([update RDS's security group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html#CHAP_SettingUp.SecurityGroup) to accept inbound TCP connections from ECS's security group)

If all went as planned, you can navigate to the running site. (Also, need to open up ECS security group to listen for HTTPS.)

## Helpful links

Docker & ECS:

+ [Take Containers From Development To Amazon ECS](https://docs.bitnami.com/aws/how-to/ecs-rds-tutorial/)
+ [Docker for Beginners](https://docker-curriculum.com)

General AWS:

+ [Migrating DNS Service for a Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-inactive.html)
+ [Configuring Amazon Route 53 to Route Traffic to an Amazon EC2 Instance](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-ec2-instance.html)

Django REST Framework & Social Auth:

+ [Django OAuth Toolkit with Django REST Framework Tutorial](https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/rest-framework.html)
+ [Django REST Framework Social Oauth2 Facebook Example](https://github.com/PhilipGarnero/django-rest-framework-social-oauth2#facebook-example)
+ [dry-rest-permissions](https://github.com/dbkaplan/dry-rest-permissions)
+ [Facebook Developer Access Tokens](https://developers.facebook.com/tools/accesstoken/)
+ [Facebook App Dashboard](https://developers.facebook.com/apps/234319953810299/dashboard/)

Other:

+ [Generating a production certificate with Let's Encrypt & ZeroSSL](https://zerossl.com)
+ [Certificates for localhost](https://letsencrypt.org/docs/certificates-for-localhost/)
+ [Make Chrome Accept a Self-Signed Certificate (on OSX)](https://www.accuweaver.com/2014/09/19/make-chrome-accept-a-self-signed-certificate-on-osx/)
+ [GeoDjango](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/)
+ [Tinder API](https://gist.github.com/rtt/10403467)


