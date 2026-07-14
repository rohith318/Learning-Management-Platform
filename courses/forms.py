from django import forms
from accounts.models import User
from .models import Course, Lesson, Enrollment, Progress


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = [
            "title",
            "description",
            "instructor",
            "status",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "instructor": forms.Select(
                attrs={"class": "form-select"}
            ),
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["instructor"].queryset = User.objects.filter(
            role="instructor"
        )


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = [
            "course",
            "title",
            "content",
            "video_url",
        ]

        widgets = {
            "course": forms.Select(
                attrs={"class": "form-select"}
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),
            "video_url": forms.URLInput(
                attrs={"class": "form-control"}
            ),
        }


class EnrollmentForm(forms.ModelForm):

    class Meta:
        model = Enrollment
        fields = [
            "user",
            "course",
        ]

        widgets = {
            "user": forms.Select(
                attrs={"class": "form-select"}
            ),
            "course": forms.Select(
                attrs={"class": "form-select"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["user"].queryset = User.objects.filter(
            role="student"
        )

        self.fields["course"].queryset = Course.objects.all()


class ProgressForm(forms.ModelForm):

    class Meta:
        model = Progress
        fields = [
            "enrollment",
            "completed_lessons",
            "progress_percent",
        ]

        widgets = {
            "enrollment": forms.Select(
                attrs={"class": "form-select"}
            ),
            "completed_lessons": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "progress_percent": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["enrollment"].queryset = Enrollment.objects.all()