def to_b64_chunk(text_string):
    new_string = ''
    lookup_string='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    additional = 0
    shift = 2

    for character in text_string:
        char = ord(character)
        new_string+=lookup_string[(additional<<(8-shift))|(char>>(shift))]
        additional = char&((1<<shift)-1)
        shift+=2

    new_string+=lookup_string[additional]

    return new_string


def to_b64_rest(text_string):
    new_string = ''
    lookup_string='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    length = len(text_string)
    additional = 0
    shift = 2

    for character in text_string:
        char = ord(character)
        new_string+=lookup_string[(additional<<(8-shift))|(char>>(shift))]
        additional = char&((1<<shift)-1)
        shift+=2

    new_string+=lookup_string[additional<<(8-shift)]

    if shift == 4:
        new_string+='='
    new_string+='='
    return new_string

def to_b64(text_string):
    chunk_start = 0
    new_string = ''
    for chunk_index in range(len(text_string)//3):
        new_string+=to_b64_chunk(text_string[chunk_start:chunk_start+3])
        chunk_start += 3

    if len(text_string)%3 != 0:
        new_string+=to_b64_rest(text_string[chunk_start:])
    return new_string

new_string = to_b64('With the other special characters and control codes filled in, ASCII was published as ASA X3.4-1963,[5][11] leaving 28 code positions without any assigned meaning, reserved for future standardization, and one unassigned control code.[2]:66, 245 There was some debate at the time whether there should be more control characters rather than the lowercase alphabet.[2]:435 The indecision did not last long: during May 1963 the CCITT Working Party on the New Telegraph Alphabet proposed to assign lowercase characters to sticks[a][12] 6 and 7,[13] and International Organization for Standardization TC 97 SC 2 voted during October to incorporate the change into its draft standard.[14] The X3.2.4 task group voted its approval for the change to ASCII at its May 1963 meeting.[15] Locating the lowercase letters in sticks[a][12] 6 and 7 caused the characters to differ in bit pattern from the upper case by a single bit, which simplified case-insensitive character matching and the construction of keyboards and printers.')
print(new_string)
test_string = 'V2l0aCB0aGUgb3RoZXIgc3BlY2lhbCBjaGFyYWN0ZXJzIGFuZCBjb250cm9sIGNvZGVzIGZpbGxlZCBpbiwgQVNDSUkgd2FzIHB1Ymxpc2hlZCBhcyBBU0EgWDMuNC0xOTYzLFs1XVsxMV0gbGVhdmluZyAyOCBjb2RlIHBvc2l0aW9ucyB3aXRob3V0IGFueSBhc3NpZ25lZCBtZWFuaW5nLCByZXNlcnZlZCBmb3IgZnV0dXJlIHN0YW5kYXJkaXphdGlvbiwgYW5kIG9uZSB1bmFzc2lnbmVkIGNvbnRyb2wgY29kZS5bMl06NjYsIDI0NSBUaGVyZSB3YXMgc29tZSBkZWJhdGUgYXQgdGhlIHRpbWUgd2hldGhlciB0aGVyZSBzaG91bGQgYmUgbW9yZSBjb250cm9sIGNoYXJhY3RlcnMgcmF0aGVyIHRoYW4gdGhlIGxvd2VyY2FzZSBhbHBoYWJldC5bMl06NDM1IFRoZSBpbmRlY2lzaW9uIGRpZCBub3QgbGFzdCBsb25nOiBkdXJpbmcgTWF5IDE5NjMgdGhlIENDSVRUIFdvcmtpbmcgUGFydHkgb24gdGhlIE5ldyBUZWxlZ3JhcGggQWxwaGFiZXQgcHJvcG9zZWQgdG8gYXNzaWduIGxvd2VyY2FzZSBjaGFyYWN0ZXJzIHRvIHN0aWNrc1thXVsxMl0gNiBhbmQgNyxbMTNdIGFuZCBJbnRlcm5hdGlvbmFsIE9yZ2FuaXphdGlvbiBmb3IgU3RhbmRhcmRpemF0aW9uIFRDIDk3IFNDIDIgdm90ZWQgZHVyaW5nIE9jdG9iZXIgdG8gaW5jb3Jwb3JhdGUgdGhlIGNoYW5nZSBpbnRvIGl0cyBkcmFmdCBzdGFuZGFyZC5bMTRdIFRoZSBYMy4yLjQgdGFzayBncm91cCB2b3RlZCBpdHMgYXBwcm92YWwgZm9yIHRoZSBjaGFuZ2UgdG8gQVNDSUkgYXQgaXRzIE1heSAxOTYzIG1lZXRpbmcuWzE1XSBMb2NhdGluZyB0aGUgbG93ZXJjYXNlIGxldHRlcnMgaW4gc3RpY2tzW2FdWzEyXSA2IGFuZCA3IGNhdXNlZCB0aGUgY2hhcmFjdGVycyB0byBkaWZmZXIgaW4gYml0IHBhdHRlcm4gZnJvbSB0aGUgdXBwZXIgY2FzZSBieSBhIHNpbmdsZSBiaXQsIHdoaWNoIHNpbXBsaWZpZWQgY2FzZS1pbnNlbnNpdGl2ZSBjaGFyYWN0ZXIgbWF0Y2hpbmcgYW5kIHRoZSBjb25zdHJ1Y3Rpb24gb2Yga2V5Ym9hcmRzIGFuZCBwcmludGVycy4='
print(test_string)
print('')
print(new_string==test_string)
