import account
import main
import common


def main_run():
    print("************************")
    print("Welcome to Login Page")
    print("************************")
    try:
        """
        common.chose_operation()
        selected_value = common.select_from_options(1, 3)
        account.users_input(selected_value)
        """
        account.users_input()
        """
        while True:
            try:
                input_val = int(input("Select from menu above : "))
                if 0 < input_val <= 3:
                    account.users_input(input_val)
                    break
                else:
                    print("Invalid input! Please enter a number from 1 to 3.")
            except ValueError:
                print("Invalid input! Please enter a numeric!")
                continue
        """
    except Exception as e:
        print("Encountered error! Please read message below:")
        print(str(e))
        pass
    finally:
        main.chose_operation()


if __name__ == "__main__":
    main_run()



