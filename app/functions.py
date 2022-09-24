from app.db import *


def add_ticket( ticket_number, ticket_description, ticket_status ):
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO tickets (t_code, t_description, t_status) VALUES ( %s, %s, %s ) RETURNING id;",
            (ticket_number, ticket_description, ticket_status,)
        )
        ticket_id = cur.fetchone()
        con.commit()
    except pymysql.err.IntegrityError:
        con.rollback()
        raise Exception(f"Ticket {ticket_number} already exists")
    except pymysql.err.ProgrammingError:
        con.rollback()
        raise Exception("Invalid status")
    finally:
        cur.close()
        con.close()
    return ticket_id


def get_all_tickets():
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "SELECT * FROM tickets;"
        )
        tickets = cur.fetchall()
    except Exception as err:
        raise Exception(err)
    finally:
        cur.close()
        con.close()
    return tickets


def get_single_ticket( ticket_id ):
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "SELECT * FROM tickets WHERE id = %s;",
            (ticket_id,)
        )
        ticket = cur.fetchone()
    except Exception as err:
        raise Exception(err)
    finally:
        cur.close()
        con.close()

    return ticket


def update_ticket( ticket_id, ticket_code, ticket_description, ticket_status ):
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "UPDATE tickets SET t_code = %s, t_description = %s, t_status = %s WHERE id = %s;",
            (ticket_code, ticket_description, ticket_status, ticket_id)
        )
        con.commit()
    except pymysql.err.IntegrityError:
        con.rollback()
        raise Exception(f"Ticket {ticket_code} already exists")
    except pymysql.err.ProgrammingError:
        con.rollback()
        raise Exception("Invalid status")
    finally:
        cur.close()
        cur.close()

    return True


def delete_ticket( ticket_id ):
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "DELETE FROM tickets WHERE id = %s;",
            (ticket_id,)
        )
        cur.execute(
            "DELETE FROM branches WHERE ticket_id = %s;",
            (ticket_id,)
        )
        con.commit()
    except Exception as err:
        con.rollback()
        raise Exception(err)
    finally:
        cur.close()
        con.close()

    return True


def add_branch( ticket_id, branch_name, branch_status ):
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO branches (ticket_id, b_name, b_status) VALUES ( %s, %s, %s ); RETURNING id",
            (ticket_id, branch_name, branch_status,)
        )
        branch_id = cur.fetchone()
        con.commit()
    except pymysql.err.IntegrityError:
        con.rollback()
        raise ValueError(f"Branch {branch_name} already exists")
    except pymysql.err.ProgrammingError:
        con.rollback()
        raise Exception("Invalid status")
    finally:
        cur.close()
        con.close()

    return branch_id


def get_all_branches( ticket_id ):
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "SELECT id, b_name, b_status FROM branches WHERE ticket_id = %s;",
            (ticket_id,)
        )
        branches = cur.fetchall()
    except Exception as err:
        raise Exception(err)
    finally:
        cur.close()
        con.close()
    return branches


def update_branch( branch_id, branch_name, branch_status ):
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "UPDATE branches SET b_name = %s, b_status = %s WHERE id = %s;",
            (branch_name, branch_status, branch_id,)
        )
        con.commit()
    except pymysql.err.IntegrityError:
        con.rollback()
        raise ValueError(f"Branch {branch_name} already exists")
    except pymysql.err.ProgrammingError:
        con.rollback()
        raise ValueError("Invalid Status")
    finally:
        cur.close()
        con.close()
    return True


def delete_branch( branch_id ):
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "DELETE FROM branches WHERE id = %s;",
            (branch_id,)
        )
        con.commit()
    except Exception as err:
        con.rollback()
        raise Exception(err)
    finally:
        cur.close()
        con.close()
    return True
