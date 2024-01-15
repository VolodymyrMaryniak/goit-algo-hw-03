import os
import argparse
import shutil

def parse_argv() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Copy all files from source directory to destination directory and sort them by extension.')
    parser.add_argument('-s', '--source', type=str, required=True, help='Source directory')
    parser.add_argument('-o', '--output', type=str, required=False, default='dest', help='Output directory')
    args = parser.parse_args()
    return args


def process_dir(source_dir, destination_dir):
    for el in os.listdir(source_dir):
        el_path = os.path.join(source_dir, el)

        if os.path.isdir(el_path):
            process_dir(el_path, destination_dir)
        else:
            process_file(el_path, destination_dir)

def process_file(file_path, destination_dir):
    try:
        file_extension = os.path.splitext(file_path)[1]
        sub_folder_name = file_extension[1:] if file_extension != '' else 'files_without_extension'

        extension_dir = os.path.join(destination_dir, sub_folder_name)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)
            
        shutil.copy(file_path, extension_dir)
    except Exception as e:
        print(e)

def main():
    args = parse_argv()

    source_dir = os.path.abspath(args.source)
    destination_dir = os.path.abspath(args.output)

    if not os.path.exists(source_dir):
        raise ValueError('Source directory does not exist')

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    process_dir(source_dir, destination_dir)

if __name__ == '__main__':
    main()