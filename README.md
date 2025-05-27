# TODO App

## Run the app

```bash
pip install "fastapi[standard]"
```

## Save dependencies

```bash
pip freeze > requirements.txt
```

## Create virtual environment

```bash
py -m venv venv
```

## Activate virtual environment

```bash
./venv/Scripts/activate
```

## Dynamodb container

```bash
docker run -p 8000:8000 amazon/dynamodb-local
```

## DB interface for local development

```bash
docker run -d `
  --name dynamodb-admin `
  -p 8001:8001 `
  -e DYNAMO_ENDPOINT=http://host.docker.internal:8000 `
  aaronshaf/dynamodb-admin
```