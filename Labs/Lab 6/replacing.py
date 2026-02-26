

def main():
    
    filename = input("Filename: ")
    old_word = input("Word to replace: ")
    new_word = input("Replace with: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        updated_content = content.replace(old_word, new_word)
        
        with open(filename, 'w') as file:
            file.write(updated_content)
        print("File updated successfully.")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")   
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()