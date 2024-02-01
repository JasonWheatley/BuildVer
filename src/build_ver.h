
#ifndef BUILD_VER_H
#define BUILD_VER_H

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

#endif // BUILD_VER_H
