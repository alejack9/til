# Check Ram Speed and Type

Using `dmidecode` it is possible to get RAM information.

`Type 16` gives Max Capacity information, `Type 17` provides speed and type information.

```shell
$ sudo dmidecode --type 16
...
Physical Memory Array
        Location: System Board Or Motherboard
        Use: System Memory
        Error Correction Type: None
        Maximum Capacity: 32 GB
        Error Information Handle: No Error
        Number Of Devices: 2
$ sudo dmidecode --type 17
...
Handle 0x0016, DMI type 17, 40 bytes
Memory Device
        ...
        Size: 4 GB
        ...
        Type: DDR4
        Type Detail: Synchronous
        Speed: 2133 MT/s
        ...
Handle 0x0017, DMI type 17, 40 bytes
Memory Device
        ...
        Size: 8 GB
        ...
        Type: DDR4
        Type Detail: Synchronous
        Speed: 2133 MT/s
        ...
```

[Source](https://ostechnix.com/how-to-find-out-maximum-supported-ram-in-linux/)
