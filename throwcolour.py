class bcolors:
    all = { 'NONE': '',
            'INFO': '\033[95m',
            'OK': '\033[92m',
            'WARN': '\033[93m',
            'ERR': '\033[91m',
            'BOLD': '\033[1m',
            'UNDERLINE': '\033[4m',
            'TERM': '\033[0m' }

def cthrow(message, type='INFO', formatting=None, addPrefix=True, dateTime=True):
    try:
        assert isinstance(message, str)
    except AssertionError:
        cthrow('Please ensure message is a string!', type="ERR")
        raise AssertionError

    outstr = bcolors.all[type] # Sets message type

    if dateTime:
        import time
        outstr += time.strftime("%I:%M:%S") + ' '

    if addPrefix:
        if type != "NONE":
            outstr += bcolors.all[type] + '[' + type + '] '

    if formatting is not None:
        try:
            assert isinstance(formatting, list)
        except AssertionError:
            cthrow('Please ensure formatting options are given as a list!', type="ERR")
            raise AssertionError

        for x in formatting:
            outstr += bcolors.all[x]

    outstr += message
    outstr += bcolors.all['TERM'] # Clear formatting after printing string

    print(outstr)

cthrow('no', type="OK")
