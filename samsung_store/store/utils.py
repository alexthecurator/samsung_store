import uuid

def unique_id():
    code = str(uuid.uuid4()).upper().replace('-', '')[:16]
    return code