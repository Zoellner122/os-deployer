# OS-Deployer

Welcome to OS-Deployer, a Python-based project designed to streamline and automate the process of (re)installing environments using QCOW2 images.

I started this project while reinstalling ArchLinux on my main desktop and encountered tasks that required manual intervention. Frustration set in, and I thought, "Wouldn't it be easier if I could simply copy an working image onto my computer?"

![](https://media.giphy.com/media/OOezqqxPB8aJ2/giphy.gif)

This started OS-Deployer, which aims to make this process possible, allowing for snappy deployment of an operating system onto a machine (both VM and Metal)

## What does OS-Deployer do.
OS-Deployer enables you to deploy an image onto your machine using a QCOW2 image. It assumes and will **always** assume that there are existing partitions already created and mounted on ```/mnt```

OS-Deployer will deploy the contents of the QCOW2 image onto your machine, resize the filesystems to fit the partitions, and potentially add and enable swap. It also provides the ability to change your machine's hostname.

## What doesn't OS-Deployer do.
As of now, it will **not** generate an image for you; it will require that you provide it with an preexisting image that either you've created or downloaded (e.g. cloud-images).

## What OS-Deployer might do.
As the project evolves, OS-Deployer may gain functionality to interact with package managers. Since this is an Arch-minded project, it may include support for Pacman and its helpers (Paru or Yay).

Thank you for your interest in OS-Deployer. We hope this tool simplifies and expedites your environment installation experience. Happy deploying!

## Responsible disclaimer:
Please note that OS-Deployer is a tool designed to automate the installation and deployment of operating systems. It is crucial to ensure that any licensed software or proprietary components used within the deployed environment comply with their respective licenses.

The OS-Deployer project and its contributors are not responsible for any unauthorized or improper use of licensed software within the deployed environments. It is the responsibility of the user to ensure that all software used in conjunction with OS-Deployer is appropriately licensed and used in accordance with the relevant licensing terms and conditions.

We strongly recommend that you review and comply with the licensing requirements of all software and components used within your deployed environments. Failure to do so may result in legal consequences and other potential issues.

Please use OS-Deployer responsibly and in compliance with all applicable laws and licenses.