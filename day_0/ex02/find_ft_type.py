allowed_types = ["list", "tuple", "set", "dict"]

def all_thing_is_obj(object: any) -> int:
	if not object: return
	obj_type = type(object)

	if obj_type.__name__ in allowed_types:
		print(f"{obj_type.__name__.capitalize()}: {obj_type}")
	elif obj_type.__name__ == "str":
		print(f"{object} is in the kitchen : {obj_type}")
	else:
		print("Type not found")
	return 42

