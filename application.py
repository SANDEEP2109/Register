def save_details(file_path, application_number, details):
    with open(file_path, 'a') as file:
        file.write(f"{application_number}: {details}\n")
    print("Svaed auccesfully")

def get_details(file_path, application_number):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(str(application_number) + ':'):
                return line.strip()
    return 'person not found'

def main():
    file_path = 'applications.txt'
    while True:
        print("\nmenu")
        print("1) new application")
        print("2) get details")
        print("3) Exit")
        choice = int(input("Choose the number: "))

        if choice == 1:
            application_number = input("Create application number: ")
            details = input("Enter the details in the format (Name: , age: , Phone number: , City: , Job: ): ")
            save_details(file_path, application_number, details)
        elif choice == 2:
            application_number = input("Enter application number: ")
            details = get_details(file_path, application_number)
            print(details)

        elif choice == 3:
            break
        else:
            print("Invaild number")

if __name__ == "__main__":
    main()
