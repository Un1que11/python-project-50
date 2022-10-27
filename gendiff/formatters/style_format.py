from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def style_format(diff, style):
    if style == 'stylish':
        return stylish(diff)
    else:
        return plain(diff)
