from ldap3 import Server, Connection, ALL, SUBTREE

# =========================
# CONFIG (LAB ONLY)
# =========================
LDAP_SERVER = "ldap://your-lab-domain.local"
USERNAME = "user@your-lab-domain.local"
PASSWORD = "Password123"
BASE_DN = "DC=your-lab-domain,DC=local"


def connect_ldap():
    try:
        server = Server(LDAP_SERVER, get_info=ALL)
        conn = Connection(server, user=USERNAME, password=PASSWORD, auto_bind=True)
        print("[+] Connected to LDAP server")
        return conn
    except Exception as e:
        print(f"[-] Connection failed: {e}")
        return None


def list_users(conn):
    print("\n[+] Enumerating Users...")
    conn.search(
        search_base=BASE_DN,
        search_filter="(objectClass=user)",
        search_scope=SUBTREE,
        attributes=["cn", "sAMAccountName"]
    )

    for entry in conn.entries:
        print(entry)


def list_groups(conn):
    print("\n[+] Enumerating Groups...")
    conn.search(
        search_base=BASE_DN,
        search_filter="(objectClass=group)",
        search_scope=SUBTREE,
        attributes=["cn"]
    )

    for entry in conn.entries:
        print(entry)


def basic_ldap_query(conn):
    print("\n[+] Running Custom LDAP Query (Admins)...")
    conn.search(
        search_base=BASE_DN,
        search_filter="(cn=Domain Admins)",
        search_scope=SUBTREE,
        attributes=["member"]
    )

    for entry in conn.entries:
        print(entry)


def main():
    conn = connect_ldap()
    if conn:
        list_users(conn)
        list_groups(conn)
        basic_ldap_query(conn)


if __name__ == "__main__":
    main()