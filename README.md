# AD Enumeration Tool (Safe)

This project demonstrates basic Active Directory enumeration using Python and LDAP in a controlled lab environment.

The goal is to simulate how attackers perform initial reconnaissance in an AD environment while keeping the implementation safe and non-intrusive.

---

## Features

- Enumerates domain users via LDAP queries  
- Enumerates AD groups  
- Performs targeted LDAP queries (e.g., Domain Admins group)  
- Simple automation for reconnaissance workflows  

---

## Technical Details

The tool connects to an LDAP server and performs queries against Active Directory objects.

Key concepts demonstrated:

- LDAP query structure and filters  
- Active Directory object classes (users, groups)  
- Attributes such as:
  - `cn` (Common Name)
  - `sAMAccountName`
- Search scopes (subtree enumeration)  

---

## Tech Stack

- Python  
- ldap3 library  
- Active Directory (lab setup)

---

## How to Run

1. Install dependencies:
