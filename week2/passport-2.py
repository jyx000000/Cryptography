#Euopean passport problem -2
import base64
from Crypto.Cipher import AES
def decrypt_oralce():
	A = 'ea8645d97ff725a898942aa280c43179'
	key = ''.join([chr(int(b,16)) for b in [A[i:i+2] for i in range(0, len(A), 2)]])
	text = '9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI'
	print len(text)
	iv = "00000000000000000000000000000000".decode("hex")
	aes = AES.new(key, AES.MODE_CBC,iv)
	base64_decrypted = base64.b64decode(text)
	decrypted_text = aes.decrypt(base64_decrypted)
	print(decrypted_text)
	
decrypt_oralce()