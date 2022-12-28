question = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "text": {"type": "string"},
        "title": {"type": "string"},
        "image": {"type": "string"},
        "position": {"type": "number"},
        "possibleAnswers": {"type": "array"}
    },
    "required": ["text","title","position","possibleAnswers"]
}