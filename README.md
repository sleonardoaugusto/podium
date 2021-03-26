# Podium

[![Tests](https://github.com/sleonardoaugusto/podium/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/sleonardoaugusto/podium/actions/workflows/ci-cd.yaml)

A mercado libre ranking system.

## How develop?

1. Clone this repo.
2. Create a virtualenv with Python 3.x.
3. Activate virtualenv.
4. Install dependencies.
5. Setup instance with .env.
6. Run tests.

```console
git clone git@github.com:sleonardoaugusto/podium.git
cd podium
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py test
```

### Resources

```
http://localhost:8000/best-sellers/?category=MLA420040&limit=15
http://localhost:8000/expensive-items/?category=MLA420040&limit=15
```
