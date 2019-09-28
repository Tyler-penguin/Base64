def from_b64_chunk(b64_string):
    new_string = ''
    lookup_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51,'0':52,'1':53,'2':54,'3':55,'4':56,'5':57,'6':58,'7':59,'8':60,'9':61,'+':62,'/':63}

    additional = lookup_dict[b64_string[0]]
    shift = 4
    for character in b64_string[1:]:
        char = lookup_dict[character]
        new_string+=chr((additional<<(6-shift))|char>>shift)
        additional = char&((1<<shift)-1)
        shift-=2

    return new_string

def from_b64_rest(b64_string):
    if b64_string[-1] != '=':
        return from_b64_chunk(b64_string)

    new_string = ''
    lookup_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51,'0':52,'1':53,'2':54,'3':55,'4':56,'5':57,'6':58,'7':59,'8':60,'9':61,'+':62,'/':63}

    additional = lookup_dict[b64_string[0]]
    char = lookup_dict[b64_string[1]]
    new_string+=chr((additional<<2)|char>>4)

    if b64_string[2] != '=':
         additional = char&0b1111
         char = lookup_dict[b64_string[2]]
         new_string+=chr((additional<<4)|char>>2)

    return new_string

def from_b64(b64_string):
    chunk_start = 0
    new_string = ''
    for i in range(len(b64_string)//4-1):
        new_string+=from_b64_chunk(b64_string[chunk_start:chunk_start+4])
        chunk_start += 4

    new_string+=from_b64_rest(b64_string[chunk_start:])
    return new_string

new_string = from_b64('V2l0aCB0aGUgb3RoZXIgc3BlY2lhbCBjaGFyYWN0ZXJzIGFuZCBjb250cm9sIGNvZGVzIGZpbGxlZCBpbiwgQVNDSUkgd2FzIHB1Ymxpc2hlZCBhcyBBU0EgWDMuNC0xOTYzLFs1XVsxMV0gbGVhdmluZyAyOCBjb2RlIHBvc2l0aW9ucyB3aXRob3V0IGFueSBhc3NpZ25lZCBtZWFuaW5nLCByZXNlcnZlZCBmb3IgZnV0dXJlIHN0YW5kYXJkaXphdGlvbiwgYW5kIG9uZSB1bmFzc2lnbmVkIGNvbnRyb2wgY29kZS5bMl06NjYsIDI0NSBUaGVyZSB3YXMgc29tZSBkZWJhdGUgYXQgdGhlIHRpbWUgd2hldGhlciB0aGVyZSBzaG91bGQgYmUgbW9yZSBjb250cm9sIGNoYXJhY3RlcnMgcmF0aGVyIHRoYW4gdGhlIGxvd2VyY2FzZSBhbHBoYWJldC5bMl06NDM1IFRoZSBpbmRlY2lzaW9uIGRpZCBub3QgbGFzdCBsb25nOiBkdXJpbmcgTWF5IDE5NjMgdGhlIENDSVRUIFdvcmtpbmcgUGFydHkgb24gdGhlIE5ldyBUZWxlZ3JhcGggQWxwaGFiZXQgcHJvcG9zZWQgdG8gYXNzaWduIGxvd2VyY2FzZSBjaGFyYWN0ZXJzIHRvIHN0aWNrc1thXVsxMl0gNiBhbmQgNyxbMTNdIGFuZCBJbnRlcm5hdGlvbmFsIE9yZ2FuaXphdGlvbiBmb3IgU3RhbmRhcmRpemF0aW9uIFRDIDk3IFNDIDIgdm90ZWQgZHVyaW5nIE9jdG9iZXIgdG8gaW5jb3Jwb3JhdGUgdGhlIGNoYW5nZSBpbnRvIGl0cyBkcmFmdCBzdGFuZGFyZC5bMTRdIFRoZSBYMy4yLjQgdGFzayBncm91cCB2b3RlZCBpdHMgYXBwcm92YWwgZm9yIHRoZSBjaGFuZ2UgdG8gQVNDSUkgYXQgaXRzIE1heSAxOTYzIG1lZXRpbmcuWzE1XSBMb2NhdGluZyB0aGUgbG93ZXJjYXNlIGxldHRlcnMgaW4gc3RpY2tzW2FdWzEyXSA2IGFuZCA3IGNhdXNlZCB0aGUgY2hhcmFjdGVycyB0byBkaWZmZXIgaW4gYml0IHBhdHRlcm4gZnJvbSB0aGUgdXBwZXIgY2FzZSBieSBhIHNpbmdsZSBiaXQsIHdoaWNoIHNpbXBsaWZpZWQgY2FzZS1pbnNlbnNpdGl2ZSBjaGFyYWN0ZXIgbWF0Y2hpbmcgYW5kIHRoZSBjb25zdHJ1Y3Rpb24gb2Yga2V5Ym9hcmRzIGFuZCBwcmludGVycy4=')
print(new_string)
test_string = 'With the other special characters and control codes filled in, ASCII was published as ASA X3.4-1963,[5][11] leaving 28 code positions without any assigned meaning, reserved for future standardization, and one unassigned control code.[2]:66, 245 There was some debate at the time whether there should be more control characters rather than the lowercase alphabet.[2]:435 The indecision did not last long: during May 1963 the CCITT Working Party on the New Telegraph Alphabet proposed to assign lowercase characters to sticks[a][12] 6 and 7,[13] and International Organization for Standardization TC 97 SC 2 voted during October to incorporate the change into its draft standard.[14] The X3.2.4 task group voted its approval for the change to ASCII at its May 1963 meeting.[15] Locating the lowercase letters in sticks[a][12] 6 and 7 caused the characters to differ in bit pattern from the upper case by a single bit, which simplified case-insensitive character matching and the construction of keyboards and printers.'
print(test_string)
print('')
print(new_string==test_string)
