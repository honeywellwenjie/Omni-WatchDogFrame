# Omni-WatchDogFrame Usage Guide

This document describes how to run, integrate, and interact with the Omni-WatchDogFrame watchdog system.

---

## Start the Watchdog Daemon

sudo ./omni_watchdog.py

<WATCHDOG> Omni-watchdog daemon booting  (version X.Y.Z)

For real deployment, it is recommended to switch to SystemBus mode and run omni_watchdog.py as a systemd service so that it starts automatically in the background at boot time.

## Register a Software Watchdog

sudo ./api/add_sfwatchdog  watchdog_name

## Start & Kick Watchdog

sudo ./api/kick_sfwatchdog  watchdog_name

## Change Timeout of a Software Watchdog

sudo ./api/sett_sfwatchdog  watchdog_name:seconds

## Remove a Software Watchdog

sudo ./api/del_sfwatchdog  watchdog_name

## Suggestion

put all api function into /usr/local/bin/
