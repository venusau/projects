from config import app, db 
from flask import jsonify, request
from models import Contact


@app.route('/contacts', methods=["GET"])
def get_contact():
    contacts = Contact.query.all()
    print(list(map(lambda x: x.to_json(), contacts)))
    json_contacts=list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts":json_contacts}), 200,

@app.route('/create_contact', methods=["POST"])
def create_contact():
    first_name=request.json.get("firstName")
    last_name=request.json.get("lastName")
    email=request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message":"You must include a first name, a last name and a email."}), 400, 
    
    contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message":f"Contact was not created or Something went wrong. ERROR: {str(e)}"}), 500,

    return jsonify({"message":"Contact created successfully"}), 201

@app.route('/update_contact/<int:user_id>', methods=["PATCH"])
def update_contact(user_id):
    # contact_id=request.json.get("id")
    # if not contact_id:
    #     return jsonify({"message":"You must include a contact id."}), 400,
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message":"Contact not found."}), 404
    

    data=request.json
    contact.first_name=data.get("firstName", contact.first_name)
    contact.last_name=data.get("lastName", contact.last_name)
    contact.email=data.get("email", contact.email)
    try:
        db.session.commit()
    except Exception as e:
        return jsonify({"message":f"Something went wrong , ERROR:{str(e)}"}), 500,

    return jsonify({"message":"Contact updated successfully"}), 200,


@app.route('/delete_contact/<int:user_id>', methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message":"Contact not found."}), 404
    try:
        db.session.delete(contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message":f"Something went wrong. ERROR{str(e)}"}), 500,

    return jsonify({"message":"Contact deleted successfully"}), 200,


if __name__=="__main__":
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', debug=True)
