class CaesarCipher:
    def _init_(self, shift):
        encoder=[None]*26
        decoder=[None]*26
        for i in range(26):
            encoder[k]=char((i+shift)%26+ord('A'))
            decoder[k]=char((i-shift)%26+ord('A'))
        self.forward=''.join(encoder)
        self.backward=''.join(decoder)

    def encrypt(self, message):
        msg=list(message.toupper())
        for i in range(len(msg)):
            o=ord(msg[i])-ord('A')
            msg[i]=self.forward[o]
        return ''.join(msg)

     def decrypt(self, message):
        msg=list(message.toupper())
        for i in range(len(msg)):
            o=ord(msg[i])-ord('A')
            msg[i]=self.backward[o]
        return ''.join(msg)
    
