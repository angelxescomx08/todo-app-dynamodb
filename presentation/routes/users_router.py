from fastapi import APIRouter, Query
from boto3.dynamodb.conditions import Key
from database.database import table
import json

users_router = APIRouter()


def list_users(last_evaluated_key=None):
    params = {
        "FilterExpression": Key("PK").begins_with("user#"),
        "Limit": 10,
    }
    if last_evaluated_key:
        params["ExclusiveStartKey"] = last_evaluated_key

    response = table.scan(**params)
    return response.get("Items", []), response.get("LastEvaluatedKey")


@users_router.get("/")
def get_users(last_key: str | None = Query(None)):
    exclusive_start_key = json.loads(last_key) if last_key else None

    users, new_last_key = list_users(exclusive_start_key)
    return {
        "users": users,
        "last_key": new_last_key,
    }


@users_router.post("/")
def create_user():
    return {"message": "User created"}
