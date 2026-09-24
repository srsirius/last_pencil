def pencils_input():
    string_input = input("How many pencils would you like to use:\n")
    while True:
        try:
            result = int(string_input)
            if result > 0:
                return result
            else:
                print("The number of pencils should be positive")
        except ValueError:
            print("The number of pencils should be numeric")
        string_input = input()


def name_input(names_list):
    name = input(f'Who will be the first ({names[0]}, {names[1]}):\n')
    while True:
        for id_name in names_list:
            if name.lower().capitalize() == id_name:
                return id_name
        else:
            print(f"Choose between {names_list[0]} and {names_list[1]}")
        name = input()


def pencils_remove():
    warning = "Possible values: '1', '2' or '3'"
    while True:
        pencils = input()
        try:
            pencils = int(pencils)
            if 1 <= pencils <= 3:
                return pencils
            else:
                print(warning)
        except ValueError:
            print(warning)


def chek_balance_pencils(pencils_balance):
    while True:
        pencils_del = pencils_remove()
        if pencils_balance - pencils_del < 0:
            print("Too many pencils were taken")
        else:
            return pencils_del


if __name__ == '__main__':
    names = ["John", "Jack"]
    pencils_all = pencils_input()
    name_first_player = name_input(names)
    name_index = False if name_first_player == names[0] else True

    while pencils_all > 0:
        print('|' * pencils_all)
        print(f"{names[name_index]}'s turn:")
        pencils_all -= chek_balance_pencils(pencils_all)
        name_index = not name_index

    print(f"{names[name_index]} won!")
