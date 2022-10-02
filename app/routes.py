from flask import jsonify, request
from app import app, logger

from app.utils import add_ticket, get_all_tickets, get_single_ticket, update_ticket, delete_ticket, add_branch, get_all_branches, update_branch, delete_branch
from app.decorators import token_required

import auth



@app.route( '/', methods=['GET'] )
def index():
    logger.log("Logs Running")
    return jsonify({"data": "App Running"})


@app.route( '/tickets', methods=['GET', 'POST', 'PATCH', 'DELETE'] )
@token_required
def _tickets( user_id, token ):
    if request.method == 'POST':
        request_data = request.get_json()
        if 'code' not in request_data or \
            'description' not in request_data or \
            'status' not in request_data:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid Parameters passed"
            }
        else:
            code = request_data['code']
            description = request_data['description']
            status = request_data['status']
            try:
                ticket_id = add_ticket( user_id, code, description, status )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}"
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Ticket added successfully",
                    "data": {
                        "token": token,
                        "ticket_id": ticket_id,
                    }
                }
    elif request.method == 'GET':
        try:
            tickets = get_all_tickets( user_id )
        except Exception as err:
            response = {
                "isOk": False,
                "status": 500,
                "message": f"{err}"
            }
        else:
            if tickets:
                tickets_dict = {}
                for count, ticket in enumerate(tickets):
                    tickets_dict[count] = {}
                    tickets_dict[count]["id"] = ticket['id']
                    tickets_dict[count]["code"] = ticket['t_code']
                    tickets_dict[count]["description"] = ticket['t_description']
                    tickets_dict[count]["status"] = ticket['t_status']
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Tickets fetched successfully",
                    "data": {
                        "token": token,
                        "tickets": tickets_dict
                    }
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "No tickets found",
                }
    elif request.method == 'PATCH':
        request_data = request.get_json()
        if 'ticket_id' not in request_data or \
            'code' not in request_data or \
            'description' not in request_data or \
            'status' not in request_data:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid parameters passed"
            }
        else:
            ticket_id = request_data['ticket_id']
            code = request_data['code']
            description = request_data['description']
            status = request_data['status']
            try:
                message = update_ticket( ticket_id, code, description, status )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}"
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Ticket updated successfully",
                    "data": {
                        "token": token
                    }
                }
    elif request.method == 'DELETE':
        request_data = request.get_json()
        if 'ticket_id' not in request_data:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid parameters passed"
            }
        else:
            ticket_id = request_data['ticket_id']
            try:
                message = delete_ticket( ticket_id )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}",
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Ticket deleted successfully",
                    "data": {
                        "token": token
                    }
                }
    return jsonify(response)


@app.route( '/ticket/<int:ticket_id>', methods=['GET', 'PATCH', 'DELETE'] )
@token_required
def _ticket_single( user_id, token, ticket_id ):
    if request.method == 'GET':
        try:
            ticket = get_single_ticket( ticket_id )
        except Exception as err:
            response = {
                "isOk": False,
                "status": 500,
                "message": f"{err}",
            }
        else:
            if ticket:
                ticket_dict = {}
                ticket_dict["id"] = ticket['id']
                ticket_dict["code"] = ticket['t_code']
                ticket_dict["description"] = ticket['t_description']
                ticket_dict["status"] = ticket['t_status']
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Ticket fetched successfully",
                    "data": {
                        "token": token,
                        "ticket": ticket_dict
                    }
                }
            else:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": "Ticket does not exists",
                }
    return jsonify(response)


@app.route( '/branches', methods=['GET', 'POST', 'PATCH', 'DELETE'] )
@token_required
def _branches( user_id, token ):
    if request.method == 'POST':
        request_data = request.get_json()
        if 'ticket_id' not in request_data or \
            'name' not in request_data or \
            'status' not in request_data:
            response = {
                    "isOk": False,
                    "status": 500,
                    "message": "Invalid parameters passed"
                }
        else:
            ticket_id = request_data['ticket_id']
            name = request_data['name']
            status = request_data['status']
            try:
                branch_id = add_branch( user_id, ticket_id, name, status )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}"
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Branch added successfully",
                    "data": {
                        "token": token,
                        "id": branch_id
                    }
                }
    if request.method == 'GET':
        request_data = request.get_json()
        if 'ticket_id' not in request_data:
            response = {
                    "isOk": False,
                    "status": 500,
                    "message": "Invalid parameters passed",
                }
        else:
            ticket_id = request_data['ticket_id']
            try:
                branches = get_all_branches( user_id, ticket_id )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}",
                }
            else:
                if branches:
                    branches_dict = {}
                    for count, branch in enumerate(branches):
                        branches_dict[count] = {}
                        branches_dict[count]["id"] = branch['id']
                        branches_dict[count]["name"] = branch['b_name']
                        branches_dict[count]["status"] = branch['b_status']
                    response = {
                        "isOk": True,
                        "status": 200,
                        "message": "Branches fetched successfully",
                        "data": {
                            "token": token,
                            "branches": branches_dict
                        }
                    }
                else:
                    response = {
                        "isOk": False,
                        "status": 500,
                        "message": "No Branches Found",
                    }
    if request.method == 'PATCH':
        request_data = request.get_json()
        if 'branch_id' not in request_data or \
            'name' not in request_data or \
            'status' not in request_data:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid parameters passed"
            }
        else:
            branch_id = request_data['branch_id']
            name = request_data['name']
            status = request_data['status']
            try:
                message = update_branch( branch_id, name, status )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}"
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Branch updated successfully",
                    "data": {
                        "token": token
                    }
                }
    elif request.method == "DELETE":
        request_data = request.get_json()
        if 'branch_id' not in request_data:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid parameters passed"
            }
        else:
            branch_id = request_data['branch_id']
            try:
                message = delete_branch( branch_id )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}",
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Branch deleted successfully",
                    "data": {
                        "token": token
                    }
                }
    return jsonify(response)


@app.route( '/register', methods=['POST'] )
def _resgister():
    if request.method == 'POST':
        request_data = request.get_json()
        if 'username' not in request_data or \
            'password' not in request_data or \
            'name' not in request_data or \
            len(request_data['username'].strip()) < 1 or \
            len(request_data['password'].strip()) < 1 or \
            len(request_data['name'].strip()) < 1:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid parameters passed"
            }
        else:
            username = request_data['username']
            password = request_data['password']
            name = request_data['name']
            try:
                token = auth.user.register( username, password, name )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}",
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "User added successfully",
                    "data": {
                        "token": token,
                    }
                }
    return jsonify(response)


@app.route( '/login', methods=['POST'] )
def _login():
    if request.method == 'POST':
        request_data = request.get_json()
        if 'username' not in request_data or \
           'password' not in request_data or \
           len(request_data['username'].strip()) < 1 or \
           len(request_data['password'].strip()) < 1:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid parameters passed"
            }
        else:
            username = request_data['username']
            password = request_data['password']
            try:
                token = auth.user.login( username, password )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}",
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "User login successfully",
                    "data": {
                        "token": token
                    }
                }
    return jsonify(response)


@app.route( '/logout', methods=['POST'] )
def _logout():
    if request.method == 'POST':
        request_data = request.get_json()
        if 'token' not in request_data or \
           len(request_data['token'].strip()) < 1:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid parameters passed"
            }
        else:
            token = request_data['token']
            try:
                auth.user.logout( token )
            except Exception as err:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": f"{err}",
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "User logout successfully"
                }
    return jsonify(response)
