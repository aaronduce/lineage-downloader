![lineage-downloader](https://i.imgur.com/cBL0JDN.png)

---

A downloader that utilises the Lineage API for acquiring LineageOS for devices.

This is a tweaked version of [u/meganukebmp's version](https://gist.github.com/meganukebmp/1a9961996a90a3a17320f9ed11a7daa4), but with some SSL changes integrated to compensate for some of the ways that SSL and caching works in relation to Lineage's API server.

The new version now caches the SSL from the first API request to prevent crashes later on due to invalid SSL errors. 

### Usage

To use the program, provide the devices.txt file with device names that you are looking to download, and change the version number to the one you want, then run the LineageDownloader.py script.

This program relies on Python 3 and will not work on Python 2.
