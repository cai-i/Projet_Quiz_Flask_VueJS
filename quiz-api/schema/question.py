question = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "text": {"type": "string"},
        "title": {"type": "string"},
        "image": {"type": "string"},
        "position": {"type": "number"},
        "possibleAnswers": {"type": "array"}
    },
    "required": ["id","text","title","position","position","possibleAnswers"]
}