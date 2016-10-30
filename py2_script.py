#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def main():
    os.system("yum -y install mariadb")
    os.system("mysql -u root")
    # os.system("yum -y install mariadb && mysql -u root")
    # якщо 1 ок тоді викон 2 

if __name__ == '__main__':
    main()
