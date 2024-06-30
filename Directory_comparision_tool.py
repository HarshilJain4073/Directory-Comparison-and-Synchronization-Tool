import os
import sys
import shutil
import filecmp
import logging

def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='Comparison.log')

def compare_file_size(dcmp):
    try:
        for files in dcmp.common_files:
            file1 = os.path.join(dcmp.left, files)
            file2 = os.path.join(dcmp.right, files)
            size1 = os.path.getsize(file1)
            size2 = os.path.getsize(file2)
            if size1 != size2:
                logging.info(f"Size differs for file {files}: {size1} bytes in {dcmp.left} and {size2} bytes in {dcmp.right}")
                print(f"Size differs for file {files}: {size1} bytes in {dcmp.left} and {size2} bytes in {dcmp.right}")
            else:
                if filecmp.cmp(file1, file2):
                    logging.info(f"Files {file1} and {file2} have the same content.")
                    print(f"Files {file1} and {file2} have the same content.")

        for sub_dcmp in dcmp.subdirs.values():
            compare_file_size(sub_dcmp)

    except Exception as e:
        logging.error(f"Error found: {e}")
        print(f"Error found: {e}")

def synchronize_directories(details, path1, path2):
    try:
        ans = input("Do you want to synchronize the directories (Y/N): ")
        if ans.lower() not in ['y', 'n']:
            logging.error("Invalid input.")
            print("Please enter a valid answer.")
            return

        if ans.lower() == "y":
            ans = input("Which directory do you want to synchronize (A or B or Both): ")
            if ans.lower() not in ['a', 'b', 'both']:
                logging.error("Invalid input.")
                print("Please enter a valid answer.")
                return
            if ans.lower() == 'a':
                for file in details.right_only:
                    file_path = os.path.join(details.right, file)
                    shutil.copy(file_path, path1)
                    logging.info(f"Copied {file_path} to {path1}")
            elif ans.lower() == 'b':
                for file in details.left_only:
                    file_path = os.path.join(details.left, file)
                    shutil.copy(file_path, path2)
                    logging.info(f"Copied {file_path} to {path2}")
            else:
                for file in details.right_only:
                    file_path = os.path.join(details.right, file)
                    shutil.copy(file_path, path1)
                    logging.info(f"Copied {file_path} to {path1}")
                for file in details.left_only:
                    file_path = os.path.join(details.left, file)
                    shutil.copy(file_path, path2)
                    logging.info(f"Copied {file_path} to {path2}")
        else:
            print("Thanks for using tool.")

    except Exception as e:
        logging.error(f"Error found: {e}")
        print(f"Error found: {e}")

def comparison():
    setup_logging()
    try:
        path1 = input("Enter the path of directory A (Absolute Path): ")
        if not os.path.isdir(path1):
            logging.error(f"Directory not found at {path1}.")
            print(f"Please enter a valid absolute path. {path1} is not a valid directory.")
            return
        
        path2 = input("Enter the path of directory B (Absolute Path): ")
        if not os.path.isdir(path2):
            logging.error(f"Directory not found at {path2}.")
            print(f"Please enter a valid absolute path. {path2} is not a valid directory.")
            return
        
        details = filecmp.dircmp(path1, path2)
        
        logging.info("Files only in directory A:")
        print("Files only in directory A:")
        for file in details.left_only:
            file_path = os.path.join(details.left, file)
            logging.info(f"{file} ({os.path.getsize(file_path)} bytes)")
            print(f"{file} ({os.path.getsize(file_path)} bytes)")

        logging.info("Files only in directory B:")
        print("\nFiles only in directory B:")
        for file in details.right_only:
            file_path = os.path.join(details.right, file)
            logging.info(f"{file} ({os.path.getsize(file_path)} bytes)")
            print(f"{file} ({os.path.getsize(file_path)} bytes)")

        logging.info("Funny files:")
        print("\nFunny files:")
        for file in details.funny_files:
            logging.info(file)
            print(file)

        logging.info("Common files:")
        print("\nCommon files:")
        for file in details.common_files:
            file_path = os.path.join(details.left, file)
            logging.info(f"{file} ({os.path.getsize(file_path)} bytes)")
            print(f"{file} ({os.path.getsize(file_path)} bytes)")

        compare_file_size(details)
        synchronize_directories(details, path1, path2)

    except Exception as e:
        logging.error(f"Error found: {e}")
        print(f"Error found: {e}")

if __name__ == "__main__":
    comparison()