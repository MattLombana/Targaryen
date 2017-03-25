#! /usr/bin/env python3
import argparse


def controller(**kwargs):
    print('in controller')
    for key, value in kwargs.items():
        print('%s = %s'.format(key, value))


def main():
    # Make these args optional. If they are present, override the yaml config file
    # Passing in these arguments can be used to run multiple instances of Targaryen threads
    #  on the same machine
    parser = argparse.ArgumentParser(description='Run an instance of the Targaryen Controller')
    parser.add_argument('-l', '--log-level',
                        help='The level to log',
                        choices=['NOTSET', 'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG',
                                 'VDEBUG'])
    parser.add_argument('-s', '--send-port',
                        help='The port to send on',
                        type=int)
    parser.add_argument('-r', '--receive-port',
                        help='The port to receive on',
                        type=int)
    args = parser.parse_args()
    foo(log=args.log_level, send=args.send_port, receive=args.receive_port)

if __name__ == '__main__':
    main()
