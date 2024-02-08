import base64

import rsa


def generate():
    pub, priv = rsa.newkeys(2048)

    try:
        with open("private2.pem", "w+b") as private_file:
            private_file.write(priv.save_pkcs1("PEM"))
    except Exception as ex:
        print(f"{ex}")

    try:
        with open("public2.pem", "w+b") as public_file:
            public_file.write(pub.save_pkcs1("PEM"))
    except Exception as ex:
        print(f"{ex}")


def get_keys():
    try:
        with open("private.pem", "rb")as private_file:
            private_key = rsa.PrivateKey.load_pkcs1(private_file.read())
        with open("public.pem", "rb")as public_file:
            public_key = rsa.PublicKey.load_pkcs1(public_file.read())

        print(f"PRIVATE KEY:\t{private_key}\nPUBLIC_KEY:\t{public_key}")

        return private_key, public_key
    except Exception as ex:
        print(f"{ex}")
        return None, None


def encrypt_str(data: str = None):
    _, public_key = get_keys()
    encrypted = rsa.encrypt(data.encode("utf-8"), pub_key=public_key)
    return encrypted


def decrypt_str(data: bytes = None):
    private_key, _ = get_keys()
    decrypted = rsa.decrypt(data, priv_key=private_key).decode()
    return decrypted


if __name__ == "__main__":
    # generate()
    # get_keys()
    data = "I have a 50m, f/1.8 Prime Lens from Nikkor"
    print(f"Original Message: {data}")
    encoded = base64.b64encode(encrypt_str(data=data)).decode()
    print(f"Encoded String:\t{encoded}")
    decoded = decrypt_str(base64.b64decode(encoded))
    print(f"Decoded String:\t{decoded}")
