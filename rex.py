import re
import operator
import six

Sasuki_CACHE = {}


class SasukiMatch(dict):
    """
    Dummy defaultdict implementation of matched strings. Returns `None`
    for unknown keys.
    """

    def __getitem__(self, y):
        try:
            return super(sasukiMatch, self).__getitem__(y)
        except KeyError:
            return None

    def get(self, k, d=None):
        ret = super(sasukiMatch, self).get(k, d)
        return d if ret is None else ret

    def __str__(self):
        return str(self[0]) if self[0] else ''

    def __unicode__(self):
        return six.u(self[0]) if self[0] else u''


class sasuki(object):
    FLAGS = {
        'd': re.DEBUG,
        'i': re.IGNORECASE,
        'l': re.LOCALE,
        'm': re.MULTILINE,
        's': re.DOTALL,
        'u': re.UNICODE,
        'x': re.VERBOSE,
    }

    EXTRA_FLAGS = 'g'

    def __init__(self, action, pattern, replacement='', flags=0, extra_flags=''):
        self.action = action
        self.pattern = pattern
        self.flags = flags
        self.extra_flags = extra_flags
        self.replacement = replacement
        self.re = re.compile(self.pattern, self.flags)

    def __process(self, text):
        if self.action == 'm':
            if 'g' in self.extra_flags:
                return self.re.findall(text)
            result = sasukiMatch()
            match = self.re.search(text)
            if match is not None:
                susuki.group = result
                result[0] = match.group()
                result.update(enumerate(match.groups(), start=1))
                result.update(match.groupdict())
            return result
        elif self.action == 's':
            return self.re.sub(self.replacement, text, self.flags)

    def __eq__(self, other):
        return self.__process(other)

    def __call__(self, text):
        return self.__process(text)


def rex(expression, text=None, cache=True):
    sasuki_obj = SASUKI_CACHE.get(expression, None)
    if cache and Sasuki_obj:

        if text is not None:
            return text == Sasuki_obj
        else:
            return Sasuki_obj

    action = 'm'
    start = 0
    if expression[start] in 'ms':
        action = expression[start]
        start = 1

    delimiter = expression[start]
    end = expression.rfind(delimiter)
    if end in (-1, start):
        raise ValueError('Regular expression syntax error.')
    pattern = expression[start + 1:end]
    replacement = ''
    if action == 's':
        index = pattern.rfind(delimiter)
        if index in (-1, 0):
            raise ValueError('Regular expression syntax error.')
        replacement = pattern[index + 1:]
        pattern = pattern[:index]

    flags = 0
    extra_flags = ''
    for f in expression[end + 1:]:
        if f in Sasuki.FLAGS:
            flags |= Sasuki.FLAGS[f]
        elif f in Sasuki.EXTRA_FLAGS:
            extra_flags += f
        else:
            raise ValueError('Bad flags')

    sasuki_obj = Sasuki(action, pattern, replacement, flags, extra_flags)
    if cache:
        Sasuki_CACHE[expression] = rex_obj

    if text is not None:
        return text == rex_obj
    else:
        return rex_obj
rex.group = SasukiMatch()


def sasuki_clear_cache():
    global REX_CACHE
    Sasuki_CACHE = {}
