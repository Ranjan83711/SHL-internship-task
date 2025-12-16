def parse_assessment_text(text):
    """
    Parses assessment chunk text into structured fields.
    """
    data = {}

    lines = text.replace("\n", " ").split("Assessment Name:")
    if len(lines) < 2:
        return None

    content = lines[1]

    def extract(key, next_key=None):
        if key not in content:
            return None
        start = content.index(key) + len(key)
        if next_key and next_key in content:
            end = content.index(next_key)
            return content[start:end].strip(" :")
        return content[start:].strip(" :")

    data["name"] = extract("", "Assessment Type")
    data["type"] = extract("Assessment Type", "Skills Measured")
    data["skills"] = extract("Skills Measured", "Job Roles")
    data["roles"] = extract("Job Roles", "Description")
    data["description"] = extract("Description", "Duration")
    data["duration"] = extract("Duration")

    return data
