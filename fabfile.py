import os
import datetime

def create_archive(directory_path):
    """
    Creates a .tgz archive from the contents of the specified directory.

    Args:
        directory_path (str): The path to the directory to archive.

    Returns:
        str: The path to the generated archive file, or None if an error occurs.
    """

    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    archive_path = f'versions/web_static_{now}.tgz'

    try:
        # Create the versions directory if it doesn't exist
        os.makedirs('versions', exist_ok=True)

        # Create the archive using shutil.make_archive (if available)
        try:
            import shutil
            shutil.make_archive(archive_path, 'gztar', directory_path)
        except ImportError:
            # Fallback to using os.system if shutil is not available
            os.system(f'tar -cvzf {archive_path} {directory_path}')

        return archive_path

    except Exception as e:
        print(f"Error creating archive: {e}")
        return None

# Example usage (assuming you want to archive the 'web_static' directory)
archive_path = create_archive('web_static')

if archive_path:
    print(f"Archive created successfully: {archive_path}")
else:
    print("An error occurred while creating the archive.")
