def write_nums_to_file():
    try:
        with open("f2.txt", "w") as file:
            for i in range(1, 101):
                file.write(str(i) + "\n")
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission error")
    except Exception:
        print("Something went wrong")

def read_file_safety():
    try:
        with open("f2.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission error")
    except Exception:
        print("Something went wrong")

write_nums_to_file()
read_file_safety()
