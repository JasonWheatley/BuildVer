
#include "build_ver.h"

// Data structure
typedef struct
{
    char DateTime[DATETIME_LENGTH + 1];
    char Developer[DEVELOPER_LENGTH + 1];
    char Uuid[UUID_LENGTH + 1];
    char Version[VERSION_LENGTH + 1];
    char git_commit_hash[GIT_COMMIT_HASH_LENGTH + 1];
}VersionData_t;

// Global instance
static VersionData_t versionData =
{
    .DateTime        = "2024-01-09 13:05:14\0",
    .Developer       = "drjohnsmith\0",
    .Uuid            = "2d1eaff8-9215-471e-b311-ecaa4b0637db\0",
    .Version         = "1.2.5\0",
    .git_commit_hash = "013fdc22d63b33bdc8eba5bb4a626dc9f719b42f\0"
};

// Accessor functions
const char* GetDateTime()
{
    return versionData.DateTime;
}

const char* GetDeveloper()
{
    return versionData.Developer;
}

const char* GetUuid()
{
    return versionData.Uuid;
}

const char* GetVersion()
{
    return versionData.Version;
}

const char* GetGitHash() 
{
    return versionData.git_commit_hash;
}
