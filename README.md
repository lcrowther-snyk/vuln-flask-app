# Vulnerable Python Flask App

This is a vulnerable Python Flask application that contains a Remote Code Execution (RCE) vulnerability.

## Description

1. **Vulnerability**: The application has an RCE vulnerability due to unsanitized input being passed to `subprocess.check_output` with `shell=True`.
2. **Semgrep Detection**: Semgrep cannot find the issue due to the indirect variable exchange for `shell=use_shell`.
3. **Snyk Detection**: Snyk detects the vulnerability due to its data flow analysis technique, which is more effective than the pattern matching used by Semgrep.
4. **DAST Tool Detection**: A Dynamic Application Security Testing (DAST) tool like OWASP ZAP or Burp Suite will find the vulnerability at runtime.

## Importance of DAST and SAST

This project demonstrates the importance of using both DAST and SAST tools in your Software Development Life Cycle (SDLC) process. While SAST tools like Semgrep and Snyk analyze the source code for vulnerabilities, DAST tools test the running application to find issues that may not be apparent in the code alone.

## Usage

To run the application:

```sh
python app.py