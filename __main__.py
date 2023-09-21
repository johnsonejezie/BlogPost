import cli


def main():
    while True:
        command = input(
            "Enter command create/read/update/delete/clear/search: ")
        if command == 'create':
            cli.create_post()
        elif command == 'read':
            post_id = input(
                "Enter the post ID you want to read or leave blank: ")
            if post_id:
                cli.read_post(int(post_id))
            else:
                cli.read_post()
        elif command == 'update':
            post_id = input("Enter the post ID you want to update: ")
            cli.update_post(int(post_id))
        elif command == 'delete':
            post_id = input("Enter ID of post to delete: ")
            cli.delete_post(int(post_id))
        elif command == 'clear':
            confirm = input(
                "Please confirm you want to clear all. Enter yes/no").lower()
            if confirm == 'yes':
                cli.delete_all()
                print("All posts cleared..")
        elif command == 'search':
            search_term = input("Enter title to search: ")
            cli.search_posts(search_term)
        elif command == 'exit':
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
