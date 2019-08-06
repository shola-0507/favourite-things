from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdSVA1l_ZhPJmMMoIhvZuuhVfYT2jfKeFa7TsK9FUDy3-ldpRMFUy-hL' \
          b'O7YCDIi2EwK_8kM-FXDV0VX-yEhuhI-aYU4HRZzdSk3gx48dHD5EOr4Bz9RzsAK' \
          b'tfR5DoWYtzvyYmw3txi-aL783yDYzj-1hWaZ2Izptbc0rX322Dl7ZtiKCg='


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
