def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if len(command_split) == 3 and command_split[0] == "cp":
        file_name = command_split[1]
        copy_file_name = command_split[2]
        if file_name != copy_file_name:
            with (open(file_name, "r") as file_to_copy,
                  open(copy_file_name, "a") as file_copy):
                file_copy.write(file_to_copy.read())
