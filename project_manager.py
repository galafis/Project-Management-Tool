#!/usr/bin/env python3
"""
Project Management Tool
Modern project management application with task tracking, team collaboration, and progress monitoring.
"""

from flask import Flask, render_template_string, jsonify, request
import sqlite3
import json
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

class ProjectManager:
    def __init__(self, db_path="projects.db"):
        self.db_path = db_path
        self.init_database()
        self.load_sample_data()
    
    def init_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'active',
                created_date DATE DEFAULT CURRENT_DATE,
                due_date DATE,
                progress INTEGER DEFAULT 0
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                project_id INTEGER,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'todo',
                priority TEXT DEFAULT 'medium',
                assigned_to TEXT,
                created_date DATE DEFAULT CURRENT_DATE,
                due_date DATE,
                FOREIGN KEY (project_id) REFERENCES projects(id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def load_sample_data(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM projects")
        if cursor.fetchone()[0] > 0:
            conn.close()
            return
        
        # Sample projects
        projects = [
            (1, "Website Redesign", "Complete redesign of company website", "active", "2024-01-15", "2024-03-15", 65),
            (2, "Mobile App Development", "Develop iOS and Android mobile application", "active", "2024-02-01", "2024-06-01", 30),
            (3, "Marketing Campaign", "Q2 marketing campaign planning and execution", "planning", "2024-03-01", "2024-05-31", 15)
        ]
        
        cursor.executemany("""
            INSERT INTO projects (id, name, description, status, created_date, due_date, progress)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, projects)
        
        # Sample tasks
        tasks = [
            (1, 1, "Design mockups", "Create initial design mockups", "completed", "high", "John Doe", "2024-01-16", "2024-01-25"),
            (2, 1, "Frontend development", "Implement responsive frontend", "in_progress", "high", "Jane Smith", "2024-01-26", "2024-02-15"),
            (3, 1, "Backend integration", "Connect frontend with backend APIs", "todo", "medium", "Bob Johnson", "2024-02-16", "2024-03-01"),
            (4, 2, "Market research", "Research target audience and competitors", "completed", "medium", "Alice Brown", "2024-02-02", "2024-02-10"),
            (5, 2, "UI/UX design", "Design mobile app interface", "in_progress", "high", "Charlie Wilson", "2024-02-11", "2024-02-28"),
            (6, 3, "Campaign strategy", "Develop marketing strategy", "todo", "high", "Diana Davis", "2024-03-02", "2024-03-15")
        ]
        
        cursor.executemany("""
            INSERT INTO tasks (id, project_id, title, description, status, priority, assigned_to, created_date, due_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tasks)
        
        conn.commit()
        conn.close()
    
    def get_dashboard_data(self):
        conn = sqlite3.connect(self.db_path)
        
        # Project statistics
        projects_df = conn.execute("SELECT * FROM projects").fetchall()
        tasks_df = conn.execute("SELECT * FROM tasks").fetchall()
        
        total_projects = len(projects_df)
        active_projects = len([p for p in projects_df if p[3] == 'active'])
        total_tasks = len(tasks_df)
        completed_tasks = len([t for t in tasks_df if t[4] == 'completed'])
        
        conn.close()
        
        return {
            'total_projects': total_projects,
            'active_projects': active_projects,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'completion_rate': (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        }

manager = ProjectManager()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Management Tool</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        .header { background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; }
        .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .metric-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 15px; padding: 25px; text-align: center; }
        .metric-value { font-size: 2.5rem; font-weight: bold; margin-bottom: 10px; }
        .metric-label { font-size: 1rem; opacity: 0.9; }
        .card { background: white; border-radius: 15px; padding: 25px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        .btn { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: 600; margin: 5px; }
        .btn:hover { opacity: 0.9; }
        .data-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        .data-table th, .data-table td { padding: 12px; text-align: left; border-bottom: 1px solid #e0e0e0; }
        .data-table th { background: #f8f9fa; font-weight: 600; }
        .status-active { color: #27ae60; font-weight: bold; }
        .status-completed { color: #3498db; font-weight: bold; }
        .status-planning { color: #f39c12; font-weight: bold; }
        .priority-high { color: #e74c3c; font-weight: bold; }
        .priority-medium { color: #f39c12; font-weight: bold; }
        .priority-low { color: #27ae60; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Project Management Tool</h1>
            <p>Manage projects, track tasks, and monitor progress</p>
        </div>
        
        <div class="dashboard-grid" id="metricsGrid">
            <!-- Metrics will be populated here -->
        </div>
        
        <div class="card">
            <h3>📋 Recent Projects</h3>
            <button onclick="loadProjects()" class="btn">🔄 Refresh Projects</button>
            <table class="data-table" id="projectsTable">
                <thead>
                    <tr>
                        <th>Project Name</th>
                        <th>Status</th>
                        <th>Progress</th>
                        <th>Due Date</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="projectsBody">
                    <!-- Projects will be populated here -->
                </tbody>
            </table>
        </div>
        
        <div class="card">
            <h3>✅ Task Overview</h3>
            <button onclick="loadTasks()" class="btn">🔄 Refresh Tasks</button>
            <table class="data-table" id="tasksTable">
                <thead>
                    <tr>
                        <th>Task</th>
                        <th>Project</th>
                        <th>Status</th>
                        <th>Priority</th>
                        <th>Assigned To</th>
                        <th>Due Date</th>
                    </tr>
                </thead>
                <tbody id="tasksBody">
                    <!-- Tasks will be populated here -->
                </tbody>
            </table>
        </div>
    </div>

    <script>
        async function loadDashboard() {
            try {
                const response = await fetch('/api/dashboard');
                const data = await response.json();
                
                document.getElementById('metricsGrid').innerHTML = `
                    <div class="metric-card">
                        <div class="metric-value">${data.total_projects}</div>
                        <div class="metric-label">Total Projects</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">${data.active_projects}</div>
                        <div class="metric-label">Active Projects</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">${data.total_tasks}</div>
                        <div class="metric-label">Total Tasks</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">${data.completion_rate.toFixed(1)}%</div>
                        <div class="metric-label">Completion Rate</div>
                    </div>
                `;
            } catch (error) {
                console.error('Error loading dashboard:', error);
            }
        }
        
        async function loadProjects() {
            try {
                const response = await fetch('/api/projects');
                const projects = await response.json();
                
                document.getElementById('projectsBody').innerHTML = projects.map(project => `
                    <tr>
                        <td><strong>${project[1]}</strong><br><small>${project[2]}</small></td>
                        <td class="status-${project[3]}">${project[3].toUpperCase()}</td>
                        <td>${project[6]}%</td>
                        <td>${project[5] || 'No due date'}</td>
                        <td><button class="btn" onclick="viewProject(${project[0]})">View</button></td>
                    </tr>
                `).join('');
            } catch (error) {
                console.error('Error loading projects:', error);
            }
        }
        
        async function loadTasks() {
            try {
                const response = await fetch('/api/tasks');
                const tasks = await response.json();
                
                document.getElementById('tasksBody').innerHTML = tasks.map(task => `
                    <tr>
                        <td><strong>${task[2]}</strong><br><small>${task[3]}</small></td>
                        <td>Project ${task[1]}</td>
                        <td class="status-${task[4]}">${task[4].replace('_', ' ').toUpperCase()}</td>
                        <td class="priority-${task[5]}">${task[5].toUpperCase()}</td>
                        <td>${task[6] || 'Unassigned'}</td>
                        <td>${task[8] || 'No due date'}</td>
                    </tr>
                `).join('');
            } catch (error) {
                console.error('Error loading tasks:', error);
            }
        }
        
        function viewProject(projectId) {
            alert(`Viewing project ${projectId} - Feature coming soon!`);
        }
        
        // Load data on page load
        document.addEventListener('DOMContentLoaded', function() {
            loadDashboard();
            loadProjects();
            loadTasks();
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/dashboard')
def get_dashboard():
    return jsonify(manager.get_dashboard_data())

@app.route('/api/projects')
def get_projects():
    conn = sqlite3.connect(manager.db_path)
    projects = conn.execute("SELECT * FROM projects ORDER BY created_date DESC").fetchall()
    conn.close()
    return jsonify(projects)

@app.route('/api/tasks')
def get_tasks():
    conn = sqlite3.connect(manager.db_path)
    tasks = conn.execute("SELECT * FROM tasks ORDER BY created_date DESC").fetchall()
    conn.close()
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

