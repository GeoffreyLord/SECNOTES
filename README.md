# SECNOTES: Security Notes
**Created By**: Geoffrey G. Lord

**Created On**: Oct 22 2024

**Description**: 
-
This repo is to be used to reference infromation that pertains to security testing and evaluation. In this repo, one will find brief notes and examples of common security findings, usage of common tools, and scripting examples. Listed below is a brief discription of the contents of each directory. 


- **Web_Security_Notes**: Contains notes on common web security vulnerabilities. Most information corresponds to the Portswingger Academy Learning Paths. This directory can serve as a starting point for web application testing. 

- **Scripting_Notes**: This directory contains scripting examples that may may be used for security testing. (API Call Example, Data Parsing Example...)

- **Security_Testing_Tools**: In this directory are notes on common security evaluation tools (SAST, DAST, Fuzzing...)

- **Security_Control_Tools**: This directory contains notes on non-testing security tooling. (IPTables, Auditd...)

- **MSC_Notes**: This directory contains random notes. (Bash & Powershell Commands)

**Tempest**:
-
In addition to security notes, this repo contains a dockerfile called Tempest. This dockerfile contains common dependencies and tooling that may prove useful for security testing. 

**To Built**: ```docker build --tag tempest .```

**To Run**: ```docker run --rm -it tempest```


*Note*: This repo is a living sheet of notest. Changes and improvements are to be expected. 
