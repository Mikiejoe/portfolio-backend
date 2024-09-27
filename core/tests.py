from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# import TestCase
from django.test import TestCase
from core.models import Project, Emails


class ModelTests(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="projects1",
            technology="projects1 technology",
            overview="projects1 overview",
            key_features="projects1 key features",
            development="projects1 development",
            conclusion="projects1 conclusion",
            github_url="https://www.github.com/projects1",
            live_url="https://www.projects1.com",
        )
        self.email = Emails.objects.create(
            subject="subject1",
            name="name1",
            message="message1",
            email="test@gmail.com",
        )

    def test_project_model(self):
        """ "
        test model creation
        test string representation
        """
        p = self.project
        self.assertTrue(isinstance(p, Project))
        self.assertEqual(str(p), p.title)

    def test_email_model(self):
        """
        test email model creation
        test string representation
        """
        e = self.email
        self.assertTrue(isinstance(e, Emails))
        self.assertEqual(str(e), e.subject)

    def test_slug_is_generated(self):
        """
        Test that the slug is automatically generated when a project is saved without a slug
        """
        project = self.project
        self.assertEqual(project.slug, "projects1")

    def test_unique_slug_generation(self):
        """
        Test that a unique slug is generated if the same title is used for multiple projects
        """
        # Create the first project
        project1 = Project.objects.create(title="My New Project")
        self.assertEqual(project1.slug, "my-new-project")

        # Create a second project with the same title
        project2 = Project.objects.create(title="My New Project")
        self.assertEqual(project2.slug, "my-new-project-1")

        # Create a third project with the same title
        project3 = Project.objects.create(title="My New Project")
        self.assertEqual(project3.slug, "my-new-project-2")

    def test_slug_is_not_changed_if_provided(self):
        """
        Test that the slug remains unchanged if it's manually provided
        """
        project = Project.objects.create(
            title="projects1",
            technology="projects1 technology",
            overview="projects1 overview",
            key_features="projects1 key features",
            development="projects1 development",
            conclusion="projects1 conclusion",
            github_url="https://www.github.com/projects1",
            live_url="https://www.projects1.com",
            slug="custom-slug",
        )
        self.assertEqual(project.slug, "custom-slug")


class ProjectsTests(APITestCase):
    def test_list_projects(self):
        """
        Ensure we can list projects
        """
        url = reverse("project-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project(self):
        """
        Ensure we can create a project
        """
        url = reverse("project-list")
        data = {
            "title": "projects1",
            "description": "projects1 description",
            "slug": "projects1",
            "technology": "projects1 technology",
            "overview": "projects1 overview",
            "key_features": "projects1 key features",
            "development": "projects1 development",
            "conclusion": "projects1 conclusion",
            "github_url": "https://www.github.com/projects1",
            "live_url": "https://www.projects1.com",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().title, "projects1")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class EmailsTests(APITestCase):
    def test_send_email(self):
        """
        Ensure we can send email
        """
        url = reverse("send-email")
        data = {
            "subject": "subject1",
            "name": "name1",
            "message": "message1",
            "email": "omoshjoe@gmail.com",
        }
        # send email
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
