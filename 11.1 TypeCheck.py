def TypeCheck(type_of_variables1, type_of_result):
    type_of_variables = list(type_of_variables1)
    def decorator(fun):
        def new_fun(*args, **kwargs):
            #print(fun.__name__)
            #print(args, kwargs)
            #type_of_variables = list(type_of_variables1)
            #print(type_of_variables)

            total_len = len(args) + len(kwargs)
            if total_len != len(type_of_variables):
                raise TypeError("Function " + fun.__name__ + " must have " + str(len(type_of_variables)) + " arguments")

            for number, item in enumerate(args):
                if type(item) is not type_of_variables[number]:
                    raise TypeError("Type of argument " + str(number + 1) + " is not " + str(type_of_variables[number]))

            for number, kv in enumerate(kwargs.items()):
                #print(type_of_variables[number], len(args))
                if type(kv[1]) is not type_of_variables[number + len(args)]:
                    raise TypeError(
                        "Type of argument '" + str(kv[0]) + "' is not " + str(type_of_variables[number]))

            result = fun(*args, **kwargs)
            if type(result) is type_of_result:
                return fun(*args, **kwargs)
            else:
                raise TypeError("Type of result is not " + str(type_of_result))

        return new_fun

    return decorator
