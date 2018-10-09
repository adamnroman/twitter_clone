#!/usr/bin/env python3

from src import omnibus

if __name__ == '__main__':
    omnibus.run(host='0.0.0.0', port=5001, debug=True)