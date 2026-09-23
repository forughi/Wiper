# Wiper
A basic Python tool for overwriting and deleting files.

Overwrites each file with random data, renames it, then deletes it. Windows only: the path handling assumes backslashes.

Limitations: This works on spinning hard drives. On SSDs and other flash storage, wear levelling means the original data stays in physical cells that overwriting cannot reach. Copy-on-write filesystems, snapshots, journals and backups keep copies too. For those, use the drive's secure erase command (hdparm, nvme-cli, or the vendor's utility) or full-disk encryption with key destruction.
