def cipher(text, shift, encrypt=True):
    """
    Conducts the traditional caesar cipher on the string text.

    Parameters
    ----------
    text:
        Any python string value
    shift:
        Any python integer value
    encrypt:
        Default value is left shift, but setting it to False will create a right shift. 

    Returns
    -------
    The new string text after the caesar cipher has been applied to it.

    Examples
    --------
    >>> from cipher_pvp2108 import cipher
    >>> cipher('Pooja', -1)
    'OnniZ'
    >>> cipher('OnniZ', -1, False)
    'Pooja'
     """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

