from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from datetime import datetime
import os
from routes import user_route

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)


app.register_blueprint(user_route)

# app.register(user_route)
# user_route.register(app)


class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), nullable=False)
    #users = db.relationship('User', backref='UserRole', lazy=True)

    def __init__(self, role_name):
        self.role_name=role_name

    def __repr__(self):
        return '<Role %r>' % self.role_name


class User_roleSchema(ma.Schema):
	class Meta:
		fields = ('id', 'role_name')

user_role_schema = User_roleSchema(strict=True)
user_roles_schema = User_roleSchema(many=True, strict=True)


@app.route('/api/user_role',methods=['POST'])
def add_user_role():
	role_name = request.json['role_name']
	new_user_role = UserRole(role_name)
	db.session.add(new_user_role)
	db.session.commit()

	return user_role_schema.jsonify(new_user_role)

@app.route('/api/user_role/', methods=['GET'])
def get_user_role():
    all_user_role = UserRole.query.all()
    result = user_roles_schema.dump(all_user_role)
    return jsonify(result.data)

@app.route('/api/user_role/<id>', methods=['GET'])
def get_user_roles(id):
    user_role = UserRole.query.get(id)
    return user_role_schema.jsonify(user_role)

@app.route('/api/user_role/<id>', methods=['DELETE'])
def delete_user_role(id):
    user_role = UserRole.query.get(id)
    db.session.delete(user_role)
    db.session.commit()

    return user_role_schema.jsonify(user_role)


class PriorityState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    priority_value = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Priority_state %r>' % self.priority_value


class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label_value = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, label_value):
        self.label_value = label_value

    def __repr__(self):
        return '<Label %r>' % self.label_value


class LabelSchema(ma.Schema):
	class Meta:
		fields = ('id', 'label_value')


label_schema = LabelSchema(strict=True)
labels_schema = LabelSchema(many=True, strict=True)


@app.route('/api/label',methods=['POST'])
def add_label():
	label_value = request.json['label_value']
	new_label = UserRole(label_value)
	db.session.add(new_label)
	db.session.commit()

	return label_schema.jsonify(new_label)

@app.route('/api/label', methods=['GET'])
def get_label():
    all_label = Label.query.all()
    result = labels_schema.dump(all_label)
    return jsonify(result.data)

@app.route('/api/label/<id>', methods=['GET'])
def get_label_by_id(id):
    label = Label.query.get(id)
    return label_schema.jsonify(label)

@app.route('/api/label/<id>', methods=['DELETE'])
def delete_label(id):
    label = Label.query.get(id)
    db.session.delete(label)
    db.session.commit()

    return label_schema.jsonify(label)



class ProjectDeadline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deadline_name = db.Column(db.String(80), nullable=False)
    deadline_description = db.Column(db.String(600), nullable=True)
    deadline_one = db.Column(db.DateTime, nullable=False)
    deadline_two = db.Column(db.DateTime, nullable=False)

    def __init__(self, deadline_name, deadline_description, deadline_one, deadline_two):
        self.deadline_name = deadline_name
        self.deadline_description = deadline_description
        self.deadline_one = deadline_one
        self.deadline_two = deadline_two


class ProjectDeadlineSchema(ma.Schema):
	class Meta:
		fields = ('id', 'deadline_name', 'deadline_description', 'deadline_one', 'deadline_two')

ProjectDeadline_schema = ProjectDeadlineSchema(strict = True)
ProjectDeadlines_schema = ProjectDeadlineSchema(many = True, strict = True)

@app.route('/api/project_deadline',methods=['POST'])
def add_user():
    deadline_name = request.json['deadline_name']
    deadline_description = request.json['deadline_description']
    deadline_one = request.json['deadline_one']
    deadline_two = request.json['deadline_two']

    new_deadline = ProjectDeadline(deadline_name, deadline_description, deadline_one, deadline_two)
    db.session.add(new_deadline)
    db.session.commit()

    return ProjectDeadline_schema.jsonify(new_deadline)

@app.route('/api/project_deadline', methods=['GET'])
def get_all_project_deadline():
    all_project_deadline = ProjectDeadline.query.all()
    result = ProjectDeadlines_schema.dump(all_project_deadline)
    return jsonify(result.data)


@app.route('/api/project_deadline/<id>', methods=['GET'])
def get_ProjectDeadline_by_id(id):
    deadline = ProjectDeadline.query.get(id)
    return ProjectDeadline_schema.jsonify(deadline)

@app.route('/api/project_deadline/<id>', methods=['DELETE'])
def delete_ProjectDeadline(id):
    deadline = ProjectDeadline.query.get(id)
    db.session.delete(deadline)
    db.session.commit()

    return ProjectDeadline_schema.jsonify(deadline)



class ProjectPhase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phase_details = db.Column(db.String(600), nullable=True)
    phase_weight = db.Column(db.Integer, nullable=False)
    phase_status = db.Column(db.Boolean, nullable=False)
    #subphases = db.relationship('ProjectSubphase', backref='ProjecyPhase', lazy=True)

    def __init__(self, phase_details, phase_weight, phase_status):
        self.phase_details = phase_details
        self.phase_weight = phase_weight
        self.phase_status = phase_status

class ProjectPhaseSchema(ma.Schema):
	class Meta:
		fields = ('id', 'phase_details', 'phase_weight', 'phase_status')

ProjectPhase_schema = ProjectPhaseSchema(strict = True)
ProjectPhases_schema = ProjectPhaseSchema(many = True, strict = True)

@app.route('/api/project_phase',methods=['POST'])
def add_project_phase():
    phase_details = request.json['phase_details']
    phase_weight = request.json['phase_weight']
    phase_status = request.json['phase_status']
    
    new_project_phase = ProjectPhase(phase_details, phase_weight, phase_status)
    db.session.add(new_project_phase)
    db.session.commit()

    return ProjectPhase_schema.jsonify(new_project_phase)

@app.route('/api/project_phase', methods=['GET'])
def get_all_project_phase():
    all_project_phase = ProjectPhase.query.all()
    result = ProjectPhases_schema.dump(all_project_phase)
    return jsonify(result.data)


@app.route('/api/project_phase/<id>', methods=['GET'])
def get_ProjectPhase_by_id(id):
    phase = ProjectPhase.query.get(id)
    return ProjectPhase_schema.jsonify(phase)

@app.route('/api/project_phase/<id>', methods=['DELETE'])
def delete_ProjectPhase(id):
    phase = ProjectPhase.query.get(id)
    db.session.delete(phase)
    db.session.commit()

    return ProjectPhase_schema.jsonify(phase)



class ProjectSubphase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subphase_details = db.Column(db.String(600),nullable=True)
    subphase_weight = db.Column(db.Boolean, nullable=False)
    parent_phase_id = db.Column(db.Integer, nullable=False)

    def __init__(self, subphase_details, subphase_weight, parent_phase_id):
        self.subphase_details = subphase_details
        self.subphase_weight = subphase_weight
        self.parent_phase_id = parent_phase_id


class ProjectSubPhaseSchema(ma.Schema):
	class Meta:
		fields = ('id', 'subphase_details', 'subphase_weight', 'parent_phase_id')

ProjectSubPhase_schema = ProjectSubPhaseSchema(strict = True)
ProjectSubPhases_schema = ProjectSubPhaseSchema(many = True, strict = True)


@app.route('/api/project_subphase',methods=['POST'])
def add_sub_project_phase():
    subphase_details = request.json['sub_phase_details']
    subphase_weight = request.json['sub_phase_weight']
    parent_phase_id = request.json['parent_phase_id']
    
    new_project_sub_phase = ProjectSubPhase(subphase_details, subphase_weight, parent_phase_id)
    db.session.add(new_project_sub_phase)
    db.session.commit()

    return ProjectSubPhase_schema.jsonify(new_project_sub_phase)

@app.route('/api/project_subphase', methods=['GET'])
def get_all_project_sub_phase():
    all_project_sub_phase = ProjectSubPhase.query.all()
    result = ProjectSubPhases_schema.dump(all_project_sub_phase)
    return jsonify(result.data)


@app.route('/api/project_subphase/<id>', methods=['GET'])
def get_ProjectSubPhase_by_id(id):
    subphase = ProjectSubPhase.query.get(id)
    return ProjectSubPhase_schema.jsonify(subphase)

@app.route('/api/project_subphase/<id>', methods=['DELETE'])
def delete_ProjectSubPhase(id):
    subphase = ProjectSubPhase.query.get(id)
    db.session.delete(subphase)
    db.session.commit()

    return ProjectSubPhase_schema.jsonify(subphase)




class ProjectState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_state_value = db.Column(db.String(80), nullable=False)

    def __init__(self, project_state_value):
        self.project_state_value = project_state_value


class ProjectStateSchema(ma.Schema):
	class Meta:
		fields = ('id', 'project_state_value')

ProjectState_schema = ProjectStateSchema(strict = True)
ProjectStates_schema = ProjectStateSchema(many = True, strict = True)


@app.route('/api/project_state',methods=['POST'])
def add_project_state():
    project_state_value = request.json['project_state_value']

    new_project_state = ProjectState(project_state_value)
    db.session.add(new_project_state)
    db.session.commit()

    return ProjectState_schema.jsonify(new_project_state)

@app.route('/api/project_state', methods=['GET'])
def get_all_project_state():
    all_project_state = ProjectState.query.all()
    result = ProjectStates_schema.dump(all_project_state)
    return jsonify(result.data)


@app.route('/api/project_state/<id>', methods=['GET'])
def get_ProjectState_by_id(id):
    state = ProjectState.query.get(id)
    return ProjectState_schema.jsonify(state)

@app.route('/api/project_state/<id>', methods=['DELETE'])
def delete_ProjectState(id):
    state = ProjectState.query.get(id)
    db.session.delete(state)
    db.session.commit()

    return ProjectState_schema.jsonify(state)

class ProjectProduction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    production_date = db.Column(db.DateTime, nullable=False)
    production_details = db.Column(db.String, nullable=False)

    def __init__(self, production_date, production_details):
        self.production_date = production_date
        self.production_details = production_details


class ProjectProductionSchema(ma.Schema):
	class Meta:
		fields = ('id', 'production_date', 'production_details')

ProjectProduction_schema = ProjectProductionSchema(strict = True)
ProjectProductions_schema = ProjectProductionSchema(many = True, strict = True)


@app.route('/api/project_production',methods=['POST'])
def add_project_production():
    production_date = request.json['production_date']
    production_details = request.json['production_details']

    new_project_production = ProjectProduction(production_date, production_details)
    db.session.add(new_project_production)
    db.session.commit()

    return ProjectProduction_schema.jsonify(new_project_production)

@app.route('/api/project_production', methods=['GET'])
def get_project_production():
    all_project_production = ProjectProduction.query.all()
    result = ProjectProductions_schema.dump(all_project_production)
    return jsonify(result.data)


@app.route('/api/project_production/<id>', methods=['GET'])
def get_project_production_by_id(id):
    project_production = ProjectProduction.query.get(id)
    return ProjectProduction_schema.jsonify(project_production)

@app.route('/api/project_production/<id>', methods=['DELETE'])
def delete_project_production(id):
    project_production = ProjectProduction.query.get(id)
    db.session.delete(project_production)
    db.session.commit()

    return ProjectProduction_schema.jsonify(project_production)



# class ProjectConversation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     conversation_token = db.Column(db.String(80), nullable=False)
#     sent_from = db.Column(db.String())

#     def __init__(self, conversation_token, sen)

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     task_name = db.Column(db.String(80), nullable=False)
#     short_note = db.Column(db.String(180), nullable=False)
#     description = db.Column(db.String(600), nullable=False)
#     deadline = db.Column(db.DateTime, nullable=False)
#     cid = db.Column(db.String(40), nullable=False)
#     jid = db.Column(db.String(40), nullable=False)
#     created_time = db.Column(db.DateTime, nullable=False)
#     task_token = db.Column(db.String(80), nullable=False)
#     assigned_user_id = db.Column(db.Integer, db.Foreignkey('user.id'),nullable=False)
#     user = db.relationship('User', backref=db.backref('tasks',lazy=True))





@app.route('/')
def inedex():
    return 'This is index'

@app.route('/func1')
def func():
    return 'func1 is called'

if __name__ == '__main__':
  app.run(debug=True)