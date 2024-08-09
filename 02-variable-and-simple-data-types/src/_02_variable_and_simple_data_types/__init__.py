def nameExample():
   name = "ada lovelace"
   print(name.title())


def fullName(firstName: str, lastName: str) -> str:
   return f"Hello, {firstName.rstrip().title()} {lastName.rstrip().title()}"

def removeURLPrefix(url: str) -> str:
   return url.removeprefix("https://")

def removePNGExtension(image: str) -> str:
   return image.removesuffix(".png")


def strings():
   message = "Hello Python world!"
   print(message)

   message = "Hello Python Crash Course world"
   print(message)

   nameExample()

   print(fullName("craig", "broughton"))

   print(removeURLPrefix("https://google.com"))

   print(removePNGExtension("hello.png"))

# a bunch of very simple functions for numbers
def numbers():
   def add(first: int, second: int) -> float:
      return first + second
   def subtract(first: int, second: int) -> float:
      return first - second
   def multiply(first: int, second: int) -> float:
      return first * second
   def divide(first: int, second: int) -> float: 
      return first / second
   
   print(add(1, 2))
   print(subtract(4, 3))
   print(multiply(5, 2))
   print(divide(2, 3))

def main():
   strings()
   numbers()

main()