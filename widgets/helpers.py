from __future__ import division
from __future__ import unicode_literals
from wcwidth import wcwidth, wcswidth

def split_text(text, width, height, unicode_aware=True):
    """
    Split text to required dimensions.
    This will first try to split the text into multiple lines, then put a "..." on the last
    3 characters of the last line if this still doesn't fit.
    :param text: The text to split.
    :param width: The maximum width for any line.
    :param height: The maximum height for the resulting text.
    :return: A list of strings of the broken up text.
    """
    # At a high level, just try to split on whitespace for the best results.
    tokens = text.split(" ")
    result = []
    current_line = ""
    string_len = wcswidth if unicode_aware else len
    for token in tokens:
        for i, line_token in enumerate(token.split("\n")):
            if string_len(current_line + line_token) > width or i > 0:
                # Don't bother inserting completely blank lines - which should only happen on the very first
                # line (as the rest will inject whitespace/newlines)
                if len(current_line) > 0:
                    result.append(current_line.rstrip())
                current_line = line_token + " "
            else:
                current_line += line_token + " "

    # At this point we've either split nicely or have a hugely long unbroken string (e.g. because the
    # language doesn't use whitespace.  Either way, break this last line up as best we can.
    current_line = current_line.rstrip()
    while string_len(current_line) > 0:
        new_line = enforce_width(current_line, width, unicode_aware)
        result.append(new_line)
        current_line = current_line[len(new_line):]

    # Check for a height overrun and truncate.
    if len(result) > height:
        result = result[:height]
        result[height - 1] = result[height - 1][:width - 3] + "..."

    # Very small columns could be shorter than individual words - truncate
    # each line if necessary.
    for i, line in enumerate(result):
        if len(line) > width:
            result[i] = line[:width - 3] + "..."

    return result

def enforce_width(text, width, unicode_aware=True):
    """
    Enforce a displayed piece of text to be a certain number of cells wide.  This takes into
    account double-width characters used in CJK languages.
    :param text: The text to be truncated
    :param width: The screen cell width to enforce
    :return: The resulting truncated text
    """
    # Double-width strings cannot be more than twice the string length, so no need to try
    # expensive truncation if this upper bound isn't an issue.
    if 2 * len(text) < width:
        return text

    # Can still optimize performance if we are not handling unicode characters.
    if unicode_aware:
        size = 0
        for i, c in enumerate(text):
            w = wcwidth(c) if ord(c) >= 256 else 1
            if size + w > width:
                return text[0:i]
            size += w
    elif len(text) + 1 > width:
        return text[0:width]

    return text
