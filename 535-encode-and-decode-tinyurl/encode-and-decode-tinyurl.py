import hashlib
class Codec:
    def __init__(self):
        self.urls={}
    def encode(self, longUrl: str) -> str:
        hash_to = 'https://tin.e/' +hashlib.md5(longUrl.encode()).hexdigest()
        self.urls[hash_to] = longUrl
        return hash_to

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))