import os

SUBSCRIBERS_TABLE = "subscribers"
SCHEDULED_MESSAGES_TABLE = "scheduled_messages"
SCHEDULED_MESSAGES_BUCKET = os.environ.get("SCHEDULED_MESSAGES_BUCKET_NAME")