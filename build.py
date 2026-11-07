#!/usr/bin/env python3
"""Regenerates Packages, Packages.gz, Packages.bz2 and Release from debs/*.deb. Run after adding or replacing a .deb."""
import glob, gzip, bz2, hashlib, os, subprocess, datetime
here = os.path.dirname(os.path.abspath(__file__))
entries = []
for deb in sorted(glob.glob(os.path.join(here, "debs", "*.deb"))):
    control = subprocess.check_output(["dpkg-deb", "-f", deb]).decode().rstrip("\n")
    data = open(deb, "rb").read()
    extra = [
        "Filename: debs/" + os.path.basename(deb),
        "Size: %d" % len(data),
        "MD5sum: " + hashlib.md5(data).hexdigest(),
        "SHA1: " + hashlib.sha1(data).hexdigest(),
        "SHA256: " + hashlib.sha256(data).hexdigest(),
    ]
    entries.append(control + "\n" + "\n".join(extra))
packages = ("\n\n".join(entries) + "\n\n").encode()
files = {"Packages": packages, "Packages.gz": gzip.compress(packages, 9), "Packages.bz2": bz2.compress(packages, 9)}
for name, blob in files.items():
    open(os.path.join(here, name), "wb").write(blob)
def block(algo):
    return "".join(" %s %d %s\n" % (getattr(hashlib, algo)(b).hexdigest(), len(b), n) for n, b in files.items())
release = ("Origin: mr1charles\nLabel: mr1charles tweaks\nSuite: stable\nVersion: 1.0\nCodename: ios\n"
           "Architectures: iphoneos-arm\nComponents: main\nDescription: iOS 26 look for old iPhones: Island26 and Spotify Lite\n"
           "Date: %s\nMD5Sum:\n%sSHA256:\n%s" % (datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S UTC"), block("md5"), block("sha256")))
open(os.path.join(here, "Release"), "w").write(release)
print("packages:", len(entries))
