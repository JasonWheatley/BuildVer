import os
import sys
import uuid
import platform
import subprocess  # Added subprocess module
from datetime import datetime

def get_developer_name():
    system = platform.system()

    if system == "Windows":
        # On Windows, use environment variable USERNAME
        return os.getenv("USERNAME")
    elif system == "Darwin":
        # On macOS, use the current user's login name
        return os.getlogin()
    elif system == "Linux":
        # On Linux, use the current user's login name
        return os.getlogin()
    else:
        # Exit with an error message if the platform is unknown
        print(f"Error: Unsupported operating system - '{system}'. Exiting.")
        sys.exit(1)

def get_git_commit_hash():

    try:
        # Run 'git rev-parse HEAD' command to get the commit hash
        result = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
        result = result.stdout.strip()
        result = result.replace(chr(0), '\\0')
        return result
    except subprocess.CalledProcessError:
        # Git command failed, project is not a Git project
        return "NOT A GIT PROJECT\0"

def generate_c_file(file_name, output_directory, version_number):
    # Get current date & time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get developer's login name
    developer_name = get_developer_name()

    # Generate a UUID
    unique_id = str(uuid.uuid4())

    # Get Git commit hash or "NOT A GIT PROJECT"
    git_commit_hash = get_git_commit_hash()

    # Content for the C file
    c_file_content = f"""
#include "{file_name}.h"

// Data structure
typedef struct
{{
    char DateTime[DATETIME_LENGTH + 1];
    char Developer[DEVELOPER_LENGTH + 1];
    char Uuid[UUID_LENGTH + 1];
    char Version[VERSION_LENGTH + 1];
    char git_commit_hash[GIT_COMMIT_HASH_LENGTH + 1];  // +1 for null terminator
}}VersionData_t;

// Global instance
static VersionData_t versionData =
{{
    .DateTime        = "{current_datetime}\\0",
    .Developer       = "{developer_name}\\0",
    .Uuid            = "{unique_id}\\0",
    .Version         = "{version_number}\\0",
    .git_commit_hash = "{git_commit_hash}\\0"
}};

// Accessor functions
const char* GetDateTime()
{{
    return versionData.DateTime;
}}

const char* GetDeveloper()
{{
    return versionData.Developer;
}}

const char* GetUuid()
{{
    return versionData.Uuid;
}}

const char* GetVersion()
{{
    return versionData.Version;
}}

const char* GetGitHash() 
{{
    return versionData.git_commit_hash;
}}
"""

    # Content for the header file
    header_file_content = f"""
#ifndef {file_name.upper()}_H
#define {file_name.upper()}_H

// Define fixed lengths
#define DATETIME_LENGTH 20
#define DEVELOPER_LENGTH 30
#define UUID_LENGTH 36
#define VERSION_LENGTH 20
#define GIT_COMMIT_HASH_LENGTH 40  // Assuming a typical Git hash length

// Function declarations
const char* GetDateTime();
const char* GetDeveloper();
const char* GetUuid();
const char* GetVersion();
const char* GetGitHash();

#endif // {file_name.upper()}_H
"""

    # Determine the appropriate directory separator for the current platform
    directory_separator = os.path.sep

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Write the C file
    c_file_path = os.path.join(output_directory, f"{file_name}.c")
    with open(c_file_path, "w") as c_file:
        c_file.write(c_file_content)

    # Write the header file
    header_file_path = os.path.join(output_directory, f"{file_name}.h")
    with open(header_file_path, "w") as header_file:
        header_file.write(header_file_content)

    print(f"Files '{file_name}.c' and '{file_name}.h' generated successfully in the '{output_directory}' directory.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <output_directory> <version_number>")
        sys.exit(1)

    output_directory = sys.argv[1]
    version_number = sys.argv[2]

    if not os.path.isdir(output_directory):
        print(f"Error: The specified output directory '{output_directory}' is not valid.")
        sys.exit(1)

    generate_c_file("build_ver", output_directory, version_number)
