# Clickjacking (UI Redressing) Notes:

## Overview

Clickjacking (also known as UI Redressing) is an attack that tricks a user into clicking on something different than what they perceive, potentially performing unintended actions. The attack is executed by embedding a legitimate web page inside an invisible or transparent iframe and overlaying it with malicious content. When the user interacts with the page, they unintentionally interact with the legitimate page behind the malicious layer.

## How Clickjacking Works
1. Invisible/Transparent iframes:

    - A legitimate website is loaded in an iframe with opacity set to 0 or positioned off-screen.
    - Malicious content overlays the iframe, misleading the user into clicking.

2. Misleading UI Elements:

    - The attacker manipulates how a UI element appears (e.g., buttons, links) to mislead users into clicking.
    - Users believe they are clicking on visible content, but they are actually clicking on hidden UI elements inside the iframe.

## Clickjacking Attack Types
**Simple Clickjacking**
- Description: The attacker overlays a legitimate website in an invisible iframe over their malicious site.
- Goal: Trick users into performing unintended actions (e.g., liking a post, submitting a form, transferring money).
- Testing:
    - Load the vulnerable site inside an iframe.
    - Manipulate the opacity or z-index of the iframe to make it invisible.
    - Try clicking and observe if the hidden UI element is clicked.

**Likejacking**
- Description: A type of clickjacking targeting social media platforms (e.g., tricking a user into liking a post or page on Facebook).
- Goal: Increase likes, shares, or follows without user consent.
- Testing:
    - Load a social media action button (like/follow) inside an iframe.
    - Test whether clicking through the overlay performs unintended actions.

**Cursorjacking**
- Description: An attack that manipulates the position of the user's cursor, leading them to click unintended UI elements.
- Goal: Mislead users into clicking sensitive areas while thinking they are clicking harmless ones.
- Testing:
    - Inspect how the cursor is visually shifted or changed to make users believe they are interacting with something else.

**Filejacking**
- Description: A variant of clickjacking where the attacker tricks the user into uploading files by clicking hidden buttons or links.
- Goal: Force users to unknowingly perform file uploads/downloads.
- Testing:
    - Load file input forms inside iframes and see if user interactions can trigger file uploads without consent.

## Common Clickjacking Scenarios
1. Auto-Like/Follow on Social Media:

    - Users are tricked into liking or following social media profiles by clicking invisible like/follow buttons.
2. Unauthorized Transactions:

    - Users are tricked into making payments or transferring funds by clicking hidden form submission buttons on financial websites.
3. Changing Settings:

    - Attackers may trick users into changing security settings, subscribing to services, or disabling protections.


## Clickjacking Defense Mechanisms

**X-Frame-Options Header**
- Purpose: Prevent the website from being embedded in an iframe.
- Directives:
    - ```DENY```: Prevents the page from being framed by any site.
    - ```SAMEORIGIN```: Allows framing only from the same origin (domain).
    - ```ALLOW-FROM`` uri: Allows framing only from specific, trusted origins (deprecated in modern browsers).
- Testing:
    - Check the HTTP response headers for ```X-Frame-Options```.
    - Attempt to load the page in an iframe; if the header is configured correctly, the browser should block it.

**Content-Security-Policy (CSP) Frame Ancestors**
- Purpose: A modern and flexible way to control which sources can embed your site in an iframe.
- Directives:
    - ```frame-ancestors 'none'```: Disallows all framing.
    - ```frame-ancestors 'self'```: Only allows the site to be framed by itself (similar to SAMEORIGIN).
    - ```frame-ancestors https://trusted.com```: Allows framing from a specific trusted domain.
- Testing:
    - Check for Content-Security-Policy headers in the HTTP response.
    - Test embedding the site in iframes on different origins to verify proper enforcement.

**Frame Busting Scripts**
- Purpose: Use JavaScript to detect when a page is loaded in an iframe and prevent framing.
- Example:
```if (self !== top) {top.location = self.location;} ```

- Limitations:
    - Modern browsers may block frame busting scripts as a security feature.
    - Frame busting is considered less effective than proper HTTP headers (e.g., ```X-Frame-Options``` or CSP).
- Testing:
    - Check if JavaScript is preventing iframe loading by inspecting browser console errors.
    - Try disabling JavaScript and see if the site is still vulnerable to clickjacking.

## Clickjacking Exploit Techniques

**Overlapping Elements**
- Technique: Position elements in such a way that the legitimate clickable element is covered by a malicious one.
- Testing:
    - Inspect the CSS ```z-index```, ```opacity```, and ```position``` properties to see how elements are visually stacked.
    - Manipulate these properties to hide or reveal elements behind a malicious overlay.

**Full-Page Iframe Overlay**
- Technique: Load a full-screen invisible iframe over the entire page to hijack clicks.
- Testing:
    - Embed the legitimate page in a full-page iframe (using ```width: 100%```, ```height: 100%```, ```opacity: 0```).
    - Click on various parts of the page to check if hidden elements are being interacted with.

**Misleading Buttons**
- Technique: Create buttons that mimic the appearance of legitimate actions but actually trigger different events in an iframe.
- Testing:
    - Click on misleading buttons and observe if legitimate buttons behind the iframe are triggered.
    - Inspect the CSS and HTML structure for positioning tricks.


## Clickjacking Testing Checklist
1. Check for Framing Protections:

    - Look for ```X-Frame-Options``` headers.
    - Check if ```Content-Security-Policy``` (CSP) with ```frame-ancestors``` is properly configured.
2. Test Embedding in Iframes:

    - Try embedding the target page in an iframe from a different domain.
    - Manipulate iframe visibility using ```opacity```, ```z-index```, and ```position` to make it invisible.
3. Click Event Testing:

    - Click through any overlaid content and see if the user’s action is performed on a hidden iframe element.
    - Test with different browsers to ensure protections are consistent.

4. Overlay Manipulation:

    - Adjust ```opacity```, ```position```, or ```size``` of iframes to make legitimate elements hidden but still clickable.
    - Use JavaScript or CSS tools to test how elements are layered on top of each other.
5. Check for JavaScript Defenses:

    - Inspect if frame-busting scripts are present in the page’s JavaScript.
    - Try disabling JavaScript and see if the site still behaves as expected inside an iframe.

## Final Notes
- Clickjacking attacks: Often rely on poor or missing defenses like ```X-Frame-Options``` and weak or missing CSP headers.
- Mitigation: Always enforce ```X-Frame-Options``` or CSP’s ```frame-ancestors` directive to prevent framing.
- Testing approach: Focus on manipulating UI elements and clicking through to check for clickjacking vulnerabilities, especially on critical actions like payments, authentication, or social media interactions.
