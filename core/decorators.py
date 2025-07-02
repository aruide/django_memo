routes = []

def route(path):
    def decorator(obj):
        # Si c'est une classe Django CBV (possède as_view)
        if hasattr(obj, 'as_view'):
            routes.append((path, obj.as_view()))
        else:
            routes.append((path, obj))
        return obj
    return decorator

