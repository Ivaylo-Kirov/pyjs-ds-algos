import random
import string

class Codec:

    def __init__(self):
        self.urlMappings = dict()
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        chars = string.ascii_letters + string.digits

        tiny_url = "http://tinyurl.com/" + "".join([random.choice(chars) for _ in range(6)])
        self.urlMappings[tiny_url] = longUrl
        return tiny_url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urlMappings[shortUrl]

# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))

# this was gold, string import can create a list of all characters and digits
# list comprehension to now pick 6 random 'things' from that list in one line