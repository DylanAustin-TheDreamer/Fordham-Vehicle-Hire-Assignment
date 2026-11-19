def check_type(obj):
    """ Checks vehicle type and returns hire cost """

    if obj == "v":
        return 35
    elif obj == "hp":
        return 28
    elif obj == "s":
        return 22.50
    else:
        raise ValueError(f"Unknown vehicle type: {obj}")
