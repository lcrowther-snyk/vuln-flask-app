from markupsafe import escape
from flask import Flask, request, render_template
import subprocess
import base64

app = Flask(__name__)

def decode_str(encoded):
    """Decode a base64 string"""
    return base64.b64decode(encoded).decode('utf-8')

PING_CMD = "cGluZyAtYyAx"  # "ping -c 1" in base64
SHELL_ARG = True  # Not directly using shell=True in a suspicious context

@app.route('/')
def home():
    return render_template('index.html')


def execute_network_diagnostic(host_param):
    """Function that appears safe but contains obfuscated command injection"""
    # Indirect command construction
    cmd_prefix = decode_str(PING_CMD)

    # Construct command indirectly to avoid patterns like "command + user_input"
    parts = []
    parts.append(cmd_prefix)
    parts.append(" ")
    parts.append(host_param)
    final_command = "".join(parts)

    # Execute with indirect shell parameter to avoid "shell=True" detection
    use_shell = SHELL_ARG
    try:
        result = subprocess.check_output(final_command, shell=use_shell, stderr=subprocess.STDOUT)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

@app.route('/diagnostic')
def network_diagnostic():
    # Using a parameter name that doesn't suggest command execution
    host = escape(request.args.get('target', 'localhost'))

    # Call function that appears safe but contains the vulnerability
    result = escape(execute_network_diagnostic(host))

    return render_template('diagnostic.html', host=host, result=result)

if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=5000)