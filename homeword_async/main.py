import asyncio


async def read_file():
    file_names = []
    for i in range(2):
        file_name = input(f"Enter the name of text file with .txt extension{i+1}: ")
        file_names.append(file_name)

    for name in file_names:
        try:
            with open(name, "r") as file:
                content = file.read()
                print(f"Content of {name}:")
                print(content)
        except FileNotFoundError:
            print(f"File '{name}' not found.")


async def main():
    await read_file()


asyncio.run(main())
