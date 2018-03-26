# vodka-soda-server

> Casual without compromise

## Set up local dev environment

Install tools and dependencies:

```bash
# Install [homebrew](https://brew.sh/)
> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# Install [pyenv](https://github.com/pyenv/pyenv)
> brew install pyenv
> pyenv install 3.6.3
# Install [virtualenv-burrito](https://github.com/brainsik/virtualenv-burrito)
> curl -sL https://raw.githubusercontent.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL
> mkvirtualenv -p /usr/local/bin/python3.6 vodka-soda-server
# Install dependencies
> pip install -r requirements.txt
```

Add environment variables:

```bash
export DJ_DB_NAME=vodka-soda
export DJ_DB_USER=tom
export DJ_DB_PASSWORD=root
export DJ_DB_HOST=localhost
export DJ_DB_PORT=5432
export DJ_SECRET_KEY=+cg9iso$a55f3ay&)pdg3k&=lq_c*55j7oyuib=a(pi#2$oj^0
```
