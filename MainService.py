#!flask/bin/python
# API Service example
# Copyright (C) 2019  Alex Milman

from flask import Flask
from flask import request

from BusinessLogic import BusinessLogic

app = Flask(__name__)


@app.route('/Test', methods=['GET'])
def test():
    response = u''
    BusinessLogic.test()
    return response


@app.route('/legal', methods=['GET'])
def legal():
    return 'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR<BR>' \
           'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,<BR>' \
           'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE<BR>' \
           'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER<BR>' \
           'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,<BR>' \
           'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE<BR>' \
           'SOFTWARE.<BR>'


@app.route('/servicecheck', methods=['GET'])
def service_check():
    return 'OK'


def get_optional_int_param(param_name):
    param_value = request.args.get(param_name)
    if param_value:
        return int(param_value)
    return 0


def get_optional_float_param(param_name):
    param_value = request.args.get(param_name)
    if param_value:
        return float(param_value)
    return 0.0




if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)