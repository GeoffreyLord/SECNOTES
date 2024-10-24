# SECNOTES
**Created By**: Geoffrey G. Lord

**Created On**: Oct 22 2024

**Description**: 
-
This repo is to be used to reference infromation that pertains to security testing and evaluation. In this repo, brief notes and examples of common security findings, usage of common tools, and scripting examples can be found. Listed below is a brief discription of the contents of each directory. 




## Contents

1. ```1_Web_Security_Notes```:
    - **Description**: Contains notes on common web security vulnerabilities. Most information corresponds to the Portswingger Academy Learning Paths. This directory can serve as a starting point for web application testing. 
    - **Examples**: (API Testing, Clickjacking, CSRF, XSS, SQLi, Path Traversal)

2. ```2_Security_Testing_Tools```:
    - **Description**: In this directory are notes on common security evaluation tools. 
    - **Sub-Directories**: 
        - ```SAST```: Static Application Security Testing
        - ```DAST```: Dynamic Application Security Testing
        - Container/Cloud Security Testing
        - OS Security Testing
    - **Examples**: (BurpSuite, Trivy, OWASP ZAP, OpenVAS)

3. ```3_Security_Control_Tools```:
    - **Description**: This directory contains notes on non-testing security tooling. 
    - **Examples**: (IPTables, Auditd)

4. ```4_Scripting_Notes```:
    - **Description**: This directory contains scripting examples that may may be used for security testing. 
    - **Examples**: (Python API Call Script, Python CSV Parsing Script, Python Regex Search Script)

5. ```5_MSC_Tools_Notes```: 
    - **Description**: This directory contains notes on everyday tools commonly used during security evaluations. 
    - **Examples**: (Grep, Hexedit, GDB, Regex)



## Tempest:

In addition to security notes, this repo contains a dockerfile called Tempest. This dockerfile contains common dependencies and tooling that may prove useful for security testing. 

**To Built**: ```docker build --tag tempest .```

**To Run**: ```docker run --rm -it tempest```


*Note*: This repo is a living sheet of notes. Changes and improvements are to be expected. 


## TODO
- [ ] OpenVAS
- [ ] Nessus
- [ ] Security Control Tools
     - [ ] IP Tables
     - [ ] AuditD
     - [ ] SELinux
    
- [ ] More Scripting Examples
- [ ] Create Tempest