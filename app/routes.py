from flask import jsonify, request
from app import app
from app.functions import add_ticket, get_all_tickets, get_single_ticket, update_ticket, delete_ticket, add_branch, get_all_branches, update_branch, delete_branch



@app.route( '/', methods=['GET'] )
def index():
    return jsonify({"data": "App Running"})


@app.route( '/tickets', methods=['GET', 'POST', 'PATCH', 'DELETE'] )
def _tickets():
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
                ticket_id = add_ticket( code, description, status )
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
                        "ticket_id": ticket_id[0],
                    }
                }
    elif request.method == 'GET':
        try:
            tickets = get_all_tickets()
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
                    tickets_dict[count]["id"] = ticket[0]
                    tickets_dict[count]["code"] = ticket[1]
                    tickets_dict[count]["description"] = ticket[2]
                    tickets_dict[count]["status"] = ticket[3]
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Tickets fetched successfully",
                    "data": tickets_dict,
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
                }
    return jsonify(response)


@app.route( '/ticket/<int:ticket_id>', methods=['GET', 'PATCH', 'DELETE'] )
def _ticket_single( ticket_id ):
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
                ticket_dict["id"] = ticket[0]
                ticket_dict["code"] = ticket[1]
                ticket_dict["description"] = ticket[2]
                ticket_dict["status"] = ticket[3]
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Ticket fetched successfully",
                    "data": ticket_dict
                }
            else:
                response = {
                    "isOk": False,
                    "status": 500,
                    "message": "Ticket does not exists",
                }
    return jsonify(response)


@app.route( '/branches', methods=['GET', 'POST', 'PATCH', 'DELETE'] )
def _branches():
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
                branch_id = add_branch( ticket_id, name, status )
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
                        "id": branch_id,
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
                branches = get_all_branches( ticket_id )
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
                        branches_dict[count]["id"] = branch[0]
                        branches_dict[count]["name"] = branch[1]
                        branches_dict[count]["status"] = branch[2]
                    response = {
                        "isOk": True,
                        "status": 200,
                        "message": "Branches fetched successfully",
                        "data": branches_dict
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
                }
    return jsonify(response)
