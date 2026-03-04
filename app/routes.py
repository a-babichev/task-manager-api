from flask import Blueprint, request, jsonify
from .extensions import db
from .models import Task

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/tasks', methods=('GET',))
def list_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return jsonify([task.to_dict() for task in tasks])


@tasks_bp.route('/tasks', methods=('POST',))
def create_task():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    task = Task(
        title=data['title'],
        description=data.get('description'),
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201


@tasks_bp.route('/tasks/<int:task_id>', methods=('PATCH',))
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)

    db.session.commit()

    return jsonify(task.to_dict())


@tasks_bp.route('/tasks/<int:task_id>', methods=('DELETE',))
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted'})
