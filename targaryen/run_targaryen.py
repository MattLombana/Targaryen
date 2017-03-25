#! /usr/bin/env python3

from controller.controller import controller
from server.server import server
from utils.conf import machines
from utils.log import logger
from worker.worker import worker

# File to automatically run targaryen. Calls the appropriate Controller, Server, or Worker
#  functions to begin


def main():
    logger.info('Running Targaryen {0}'.format(machines['instance']['type']))
    if machines['instance']['type'] == 'controller':
        controller()
    elif machines['instance']['type'] == 'server':
        server()
    elif machines['instance']['type'] == 'worker':
        worker()

if __name__ == '__main__':
    main()
