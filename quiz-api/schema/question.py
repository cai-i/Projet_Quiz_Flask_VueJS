question = {
    "type": "object",
    "properties": {
        "text": {"type": "string"},
        "title": {"type": "string"},
        "image": {"type": "string"},
        "position": {"type": "number"},
        "possibleAnswers": {"type": "array"}
    },
    "required": ["text","title","position","possibleAnswers"]
}