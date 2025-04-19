import json


def harmonize(metadata, message):
    print("Harmonizing")
    processed_message = {
    }
    try:
        processed_message = json.loads(message)
    except Exception as e:
        processed_message = {"value": message}
    if not isinstance(processed_message, dict):
        processed_message = {"value": processed_message}
    metadata.update(processed_message)
    return metadata
