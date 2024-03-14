def input_error(func):
    """
    This function is a decorator that is used to handle exceptions that may occur during
    the execution of the function it is decorating.

    Parameters:
    func (function): The function that is being decorated

    Returns:
    function: A wrapper function that handles exceptions raised by the decorated function

    Raises:
    ValueError: If the input value is not of the correct type
    TypeError: If the input value is of the correct type but is not in the correct format
    IndexError: If the input value is of the correct format but is out of range
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)
        except TypeError:
            return "Phone number is invalid. The phone number must consist of exactly 10 digits."
        except IndexError:
            return "The command is bad. Enter a command again."
        except:
            return "Something is wrong. Enter a command again."

    return inner
