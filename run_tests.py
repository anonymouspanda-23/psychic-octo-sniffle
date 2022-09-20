import os, re

def get_python_files():
    # get files in current dir
    files_in_dir = [f for f in os.listdir('.') if os.path.isfile(f)]
    current_file = os.path.basename(__file__)
    files_in_dir.remove(current_file)


    # remove non python files
    files_in_dir = [f for f in files_in_dir if f[len(f) - 3:] == ".py"]

    # remove non test_files
    files_in_dir = [f for f in files_in_dir if "test" in f]

    # run scripts
    for f in files_in_dir:
        print()
        print(f"Running: {f}")
        exec(open(f).read())

        print()
        print('-' * 20)

get_python_files()
