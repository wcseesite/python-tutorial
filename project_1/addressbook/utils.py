def normalize_name(name):
    return ' '.join(word.capitalize() for word in name.lower().split())