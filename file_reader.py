def read_file(file_path):
   try:
       with open(file_path, 'r') as file:
           print(file.read())
   except FileNotFoundError:
       print(f"File {file_path} not found.")
if __name__ == "__main__":
   read_file('sample.txt')  