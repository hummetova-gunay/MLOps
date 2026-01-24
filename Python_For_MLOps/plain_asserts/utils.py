def str_to_bool(value):
    true_vals =['yes', 'y', '']
    false_vals = ['no', 'N']

    try:
        value = value.lower()
    except AttributeError:
        value = str(value).lower()
    if value in true_vals:
        return True
    elif value in false_vals:
        return False
    else:
        raise ValueError(f'Invalid input {value}')
    