"""
Tests for Project Management Tool using Flask test_client.
"""

import pytest
import os
import sys


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from project_manager import app, get_manager


    @pytest.fixture(autouse=True)
    def setup_manager(tmp_path):
        """Initialise ProjectManager with a temporary database for each test."""
        import project_manager
        from project_manager import ProjectManager

        db_path = str(tmp_path / "test_projects.db")
        project_manager.manager = ProjectManager(db_path=db_path)
        yield
        project_manager.manager = None


    @pytest.fixture
    def client():
        app.config["TESTING"] = True
        with app.test_client() as c:
            yield c


    class TestIndex:
        def test_get_index_returns_200(self, client):
            resp = client.get("/")
            assert resp.status_code == 200
            assert b"Project Management Tool" in resp.data


    class TestAPIProjects:
        def test_get_projects_returns_json_list(self, client):
            resp = client.get("/api/projects")
            assert resp.status_code == 200
            data = resp.get_json()
            assert isinstance(data, list)
            assert len(data) > 0


    class TestAPITasks:
        def test_get_tasks_returns_json_list(self, client):
            resp = client.get("/api/tasks")
            assert resp.status_code == 200
            data = resp.get_json()
            assert isinstance(data, list)
            assert len(data) > 0


    class TestAPIDashboard:
        def test_get_dashboard_returns_stats_dict(self, client):
            resp = client.get("/api/dashboard")
            assert resp.status_code == 200
            data = resp.get_json()
            assert isinstance(data, dict)
            for key in ("total_projects", "active_projects", "total_tasks",
                         "completed_tasks", "completion_rate"):
                assert key in data
            assert data["total_projects"] >= 1
            assert data["total_tasks"] >= 1
