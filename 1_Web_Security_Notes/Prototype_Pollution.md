# Prototype Pollution Vulnerabilities Notes:

## Overview
Prototype Pollution is a vulnerability specific to JavaScript, particularly when dealing with objects. In JavaScript, objects inherit properties and methods from a prototype, and this inheritance can be manipulated. Prototype Pollution allows attackers to modify the prototype of a base object (e.g., ```Object.prototype```), which affects all instances of that object, potentially leading to security issues like arbitrary code execution, data manipulation, or denial of service.

Prototype pollution mainly affects JavaScript environments like Node.js and browser-based JavaScript applications that rely on user-controlled input when creating or modifying objects.

## How Prototype Pollution Works
In JavaScript, each object is linked to a prototype object from which it inherits properties and methods. The prototype chain allows all objects created from the same constructor function to share common behavior. However, if an attacker is able to modify the prototype (such as ```Object.prototype```), they can inject properties that affect all objects in the system.

**Example of Prototype Pollution**:
An application might merge user-provided data into an object like this:

    const userSettings = {};
    Object.assign(userSettings, userInput);

If ```userInput``` contains dangerous keys like ```__proto__```, an attacker could alter the prototype:

    userInput = { "__proto__": { "isAdmin": true } };

This will modify the global ```Object.prototype```, leading to the ```isAdmin``` property being available on all objects:

    console.log({}.isAdmin); // true

This can lead to unauthorized access or other unexpected behavior.

## Types of Prototype Pollution Attacks
1. Direct Prototype Pollution
    - Description: Attackers directly inject properties into the ```Object.prototype``` or another prototype through user input.
    - Example:

        - ```const userInput = { "__proto__": { "isAdmin": true } }; Object.assign({}, userInput);```

        - This adds the ```isAdmin``` property to all objects created from ```Object```.

    - Impact: This can result in privilege escalation, data corruption, or unexpected behavior across the application.
2. Property Injection
    - Description: Attackers can inject properties that may lead to vulnerabilities in the application logic or trigger unexpected behavior in other parts of the system.
    - Example:
        - Injecting dangerous properties like ```constructor```, ```toString```, or overriding default object methods.
        - ```const data = { "__proto__": { "toString": () => "Hacked!" } };```
        - This could cause built-in methods like ```toString()``` to behave differently or expose sensitive data.
    - Impact: Breaking built-in methods or altering the system's behavior can lead to data leakage or the application functioning improperly.
3. Denial of Service via Prototype Pollution
    - Description: Attackers can pollute the prototype to inject properties that cause infinite loops, crashes, or resource exhaustion.
    - Example:
        - Injecting properties like ```__proto__``` with an object that causes infinite recursion.
        - ```const data = { "__proto__": { "key": {} } };```
        - ```Object.assign({}, data);```
    - Impact: This can result in a denial-of-service (DoS) attack, crashing the server or freezing the application.


## Exploitation Techniques
1. Object Merging Functions
    - Technique: Exploit functions like ```Object.assign()```, ```_.merge()```, or ```$.extend()``` that combine user input with objects.
    - Example:
        - ```const settings = {};```
        - ```Object.assign(settings, userInput);```
        = Injecting ```__proto__``` in the userInput will modify the prototype, affecting all objects.
2. Manipulating Object Prototype
    - Technique: Inject properties into ```Object.prototype``` to override default properties or add new ones.
    - Example:
        - ```const userInput = { "__proto__": { "admin": true } };```
        - ```const user = Object.assign({}, userInput);``` 
        - ```console.log(user.admin); // true```
        - ```console.log({}.admin);   // true```
    - This adds ```admin``` to the global object prototype.
3. Third-Party Libraries
    - Technique: Some third-party libraries (like Lodash or jQuery) have vulnerable functions that can be exploited for prototype pollution.
    - Example:
        - Exploiting Lodash's ```_.merge()``` function with polluted data:
        - ```const userInput = { "__proto__": { "isAdmin": true } };```
        - ```_.merge({}, userInput);```
    - This affects the global prototype chain.


## Real-World Impacts of Prototype Pollution
1. Privilege Escalation
    - Description: Attackers can add properties like ```isAdmin``` or ```role``` to the prototype, allowing them to escalate privileges in the application.
    - Example:
        - An attacker adds ```isAdmin: true``` to the prototype. All objects now have this property, allowing the attacker to access administrative functionality.
2. Application Corruption
    - Description: By injecting unexpected properties, attackers can break the expected behavior of objects, leading to corrupted data or business logic errors.
    - Example:
        - Overriding the ```toString()``` method or ```constructor``` can cause the application to behave erratically or expose sensitive information.
3. Denial of Service (DoS)
    - Description: Prototype pollution can be used to create recursive structures or crash the application by overwhelming its memory or CPU resources.
    - Example:
        - An attacker injects an infinitely recursive structure into the prototype, causing the server to crash when trying to process the polluted object.

## Defense Mechanisms Against Prototype Pollution
1. Input Validation and Sanitization
    - Description: Validate and sanitize all user input, specifically checking for dangerous keys like ```__proto__```, ```constructor```, and other prototype-related properties.
    - Best Practices:
        - Reject input that contains any of the following keys: ```__proto__```, ```prototype```, ```constructor```.
        - Use libraries that automatically sanitize input when merging objects.
2. Use Object.create(null)
    - Description: Use ```Object.create(null)``` to create objects that don’t inherit from ```Object.prototype```, making them immune to prototype pollution.
    - Best Practices:
        - Avoid using plain objects ```{}``` when dealing with user input. Instead, use ```Object.create(null)``` for safer objects.
        - ```const safeObject = Object.create(null);```
3. Limit Use of Object.assign() and Similar Functions
    - Description: Avoid using functions like ```Object.assign()``` or ```_.merge()``` without proper input sanitization, as these functions can copy properties to the prototype.
    - Best Practices:
        - If you must use these functions, ensure the input is sanitized before passing it into the function.
4. Use Secure Libraries
    - Description: Regularly update third-party libraries and use versions that are known to be secure from prototype pollution.
    - Best Practices:
        - Use security-focused tools like ```npm audit``` to identify and fix vulnerabilities in dependencies.
        - Avoid using libraries that are known to be susceptible to prototype pollution without necessary precautions.
5. Freeze Prototypes
    - Description: Use ```Object.freeze()``` to prevent further modifications to critical objects like ```Object.prototype```.
    - Best Practices:
        - Freeze the prototype of objects that should not be modified.
        - ```Object.freeze(Object.prototype);```

## Testing for Prototype Pollution
1. Manual Testing
    - Inject Polluted Input:
        - Inject input like ```{"__proto__": {"isAdmin": true}}``` and check if the prototype is affected.
        - Example:
            - ```const userInput = { "__proto__": { "isAdmin": true } };```
            - ```Object.assign({}, userInput);```
            - ```console.log({}.isAdmin); // true```
2. Automated Testing Tools
    - Prototype Pollution Scanners:
        - Use tools like HackerOne's Prototype Pollution Detection to test for vulnerable libraries and methods in your code.
    - Burp Suite Extensions:
        - Use Burp Suite with custom extensions or plugins to automate prototype pollution testing by injecting payloads and monitoring responses.
3. Review Third-Party Libraries
    - Audit Dependencies:
        - Regularly run ```npm audit``` to identify and resolve vulnerabilities in third-party dependencies that may allow prototype pollution.
        - Manually inspect commonly used libraries (e.g., Lodash, jQuery) for functions like ```merge()``` or ```extend()``` that could be vulnerable.


## Prototype Pollution Defense Checklist
1. Sanitize User Input: Validate all input, especially checking for dangerous prototype-related keys (__proto__, constructor, etc.).

2. Use Object.create(null): Create objects without a prototype to prevent inheritance from Object.prototype.

3. Avoid Vulnerable Functions: Avoid using Object.assign(), _.merge(), or similar functions with unsanitized user input.

4. Freeze Object Prototypes: Use Object.freeze() to protect critical objects from being modified.

5. Update and Audit Libraries: Regularly update third-party libraries and audit dependencies to ensure they are not vulnerable to prototype pollution.

## Final Notes
- Prototype Pollution: A significant security risk in JavaScript environments that allows attackers to manipulate object behavior, potentially leading to privilege escalation, data corruption, or denial of service.
- Mitigation: Focus on input validation, use of Object.create(null), and limiting unsafe functions like Object.assign() to prevent exploitation.
- Testing: Regularly audit third-party libraries and manually test with polluted input to detect potential vulnerabilities.