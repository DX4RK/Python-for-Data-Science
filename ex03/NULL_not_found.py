type_to_prefix = {
	"NoneType": "Nothing",
	"float": "Cheese",
	"int": "Zero",
	"str": "Empty",
	"bool": "Fake",
}

def NULL_not_found(object: any) -> int:
	obj_type = type(object)

	if object and not obj_type.__name__ == "float":
		print("Type not Found")
		return 1;

	print(f"{type_to_prefix[obj_type.__name__]}: {object} {obj_type}")
	return 0

