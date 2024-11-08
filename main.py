import os
import sys

from mock.graph import *
from img.img_to_commit import *
from git_bot.commit_bot import *

space_invader_img = "./pixel_art//Space_invader.jpg"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[1;36m"
PURPLE = "\033[1;35m"
GREEN = "\033[1;32m"
RESET = "\033[0m"


def ask_image():
    image = input(f"Enter your {PURPLE}image path {RESET}(e.g. {CYAN}'../relative/path/to/your/image'{RESET})  \n "
                  f"By default, the space invader image will be used) : ")

    if not image:
        image = space_invader_img
        print(f"{GREEN}The space invader image will be used.{RESET}")

    return image


def ask_repo_path():
    repo_path = input(f"Enter your {PURPLE} local git repository path {RESET}(e.g. {CYAN}'../dummy_repo/'{RESET}): ")
    repo_path = os.path.abspath(repo_path)

    if not os.path.exists(repo_path):
        raise ValueError(f"Error: Specified path does not exist {repo_path}, "
                         "please enter a valid path")

    if not os.path.isdir(os.path.join(repo_path, ".git")):
        raise ValueError("Error : Spécified path is not a git repository")

    return repo_path


def ask_dummy_file(repo_path):
    dummy_file = input(f"Enter your {PURPLE}dummy file's name {RESET}(e.g. {CYAN}dummy.txt{RESET}) \n"
                       f" If he doesn't exist, he will be created:")
    dummy_file_path = os.path.join(repo_path, dummy_file)

    if not os.path.isfile(dummy_file_path):
        print(f"File'{dummy_file}'does not exist. \n"
              f"{PURPLE}Creation... {RESET}")
        with open(dummy_file_path, 'w') as file:
            file.write("Dummy file for Gitxel-Art generation")
        print(f"{GREEN}File'{dummy_file}' succesfully created in the repository {repo_path}{RESET}")

    return dummy_file


def ask_year():
    year = int(input(f"Enter the {PURPLE}year {RESET}for the pixel art (e.g., {CYAN}2024{RESET}): "))
    if year < 1974:
        print(f"Can't creat comit {YELLOW}older than 1974{RESET}, please select again a {BLUE}valid year:{RESET}")
        ask_year()
    return year


def ask_preview():
    preview_input = input("The preview mode show the result of your image with a mocked contribution graph \n"
                          f"{GREEN}It doesn't generate commit.{RESET} \n"
                          f" Do you want to run in {PURPLE}preview{RESET} mode ? {CYAN}(y/n){RESET} : ").strip().lower()
    return preview_input in ("oui", "o", "yes", "y", "Yes", "Y", "Oui", "O")


def main():
    print(fr"""{PURPLE}                                        _ _            _              _    
                                       (_) |          | |            | |   
                                   __ _ _| |___  _____| |   __ _ _ __| |_  
                                  / _` | | __\ \/ / _ \ |  / _` | '__| __| 
                                 | (_| | | |_ >  <  __/ | | (_| | |  | |_  
                                  \__, |_|\__/_/\_\___|_|  \__,_|_|   \__| 
                                   __/ |      ##          ##
                                                ##      ##        
                                              ##############
                                            ####  ######  ####
                                          ######################
                                          ##  ##############  ##     
                                          ##  ##          ##  ##
                                                ####  ####{RESET}""")

    print(f"{RED}DISCLAIMER: \n {YELLOW}  Gitxel-Art is intended solely for educational and entertainment purposes. \n"
          f" {RESET}  The creator of this project disclaims any responsibility for the use of this tool, and by using it, "
          f"you agree that any consequences resulting from the generation of commits,"
          f" including but not limited to unwanted repository activity or accidental exposure of data, are solely your responsibility. \n"
          f"{YELLOW}  This tool is not endorsed by GitHub, and it is recommended that you use it only for fun or learning. \n"
          f"{RESET} Please ensure that any repositories used are private, and do not use this tool in ways that violate GitHub's Terms of Service. \n \n"
          f"{RED}Use this tool at your own risk. The creator is not liable for any damages or unexpected outcomes related to the use of this project. \n \n{RESET}")

    image = ask_image()
    repo_path = ask_repo_path()

    dummy_file = ask_dummy_file(repo_path)
    year = ask_year()

    preview = ask_preview()

    commit_grid = image_to_commit_grid(image)

    if preview:
        print(f"{GREEN}Launch preview mode{RESET}")
        generate_graph(commit_grid)

        if ask_preview():
            print(f"{GREEN}Launch preview mode{RESET}")
            generate_graph(commit_grid)
            sys.exit(0)

        print(f"{GREEN}Proceeding to commit generation{RESET}")
    else:
        print(f"{GREEN}Proceeding to commit generation{RESET}")

    generate_commits(commit_grid, year, repo_path, dummy_file)


if __name__ == "__main__":
    main()
