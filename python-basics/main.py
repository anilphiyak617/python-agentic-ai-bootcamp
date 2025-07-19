def main():
    print("Hello from python-basics!")
    read_file()

# Function to read a file
def read_file():
    with open("README.md", "r") as file:
        content = file.read()
        print("File content:",content)
    return content

if __name__ == "__main__":
    main()
