#include <stdio.h>
#include "build_ver.h"

int main(int argc, char *argv[])
{
    printf("Build Date/Time: %s\n", GetDateTime());
    printf("Developer:       %s\n", GetDeveloper());
    printf("UUID:            %s\n", GetUuid());
    printf("Version:         %s\n", GetVersion());
    printf("Git Hash:        %s\n", GetGitHash());
    printf("\n");
    
    return 0;
}
