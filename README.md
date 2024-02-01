# build_ver
## Introduction
Generates a C source &amp; header containing date, time, developer, UUID &amp; version information.

### Files Generated
* build_ver.c
* build_ver.h

### Public Functions
* `const char* GetDateTime();`
* `const char* GetDeveloper();`
* `const char* GetUuid();`
* `const char* GetVersion();`

## Usage
`python3 gen_ver.py <out dir> <version string>`

|Parameter|Explanation|
|---|---|
|`<out dir>`|Path to output directory|
|`<version string>`|Version of software than generated code will be used within|

### Example
``` shell
python3 gen_ver.py out "1.2.5"
```

## Generated Code
### build_ver.h
```c
#ifndef BUILD_VER_H
#define BUILD_VER_H

// Define fixed lengths
#define DATETIME_LENGTH 20
#define DEVELOPER_LENGTH 30
#define UUID_LENGTH 36
#define VERSION_LENGTH 20

// Function declarations
const char* GetDateTime();
const char* GetDeveloper();
const char* GetUuid();
const char* GetVersion();

#endif // BUILD_VER_H
```

### build_ver.c
```c
#include "build_ver.h"

// Data structure
typedef struct
{
    char DateTime[DATETIME_LENGTH + 1];
    char Developer[DEVELOPER_LENGTH + 1];
    char Uuid[UUID_LENGTH + 1];
    char Version[VERSION_LENGTH + 1];
}VersionData_t;

// Global instance
static VersionData_t versionData =
{
    .DateTime   = "2024-01-09 13:05:14\0",
    .Developer  = "drjohnsmith\0",
    .Uuid       = "2d1eaff8-9215-471e-b311-ecaa4b0637db\0",
    .Version    = "1.2.5\0",
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
```


## Using Generated Code

### Example Code
```c
#include <stdio.h>
#include "build_ver.h"

int main(int argc, char *argv[])
{
    printf("Build Date/Time: %s\n", GetDateTime());
    printf("Developer:       %s\n", GetDeveloper());
    printf("UUID:            %s\n", GetUuid());
    printf("Version:         %s\n", GetVersion());
    printf("\n");
    
    return 0;
}
```

### Example Code Output
```
$ build/myapp 
Build Date/Time: 2024-01-09 13:05:14
Developer:       drjohnsmith
UUID:            2d1eaff8-9215-471e-b311-ecaa4b0637db
Version:         1.2.5
```

