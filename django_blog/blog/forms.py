from django import forms
from .models import Post
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
        # التعامل مع الـ tags
        tags_str = self.cleaned_data.get("tags", "")
        if tags_str:
            tag_names = [name.strip() for name in tags_str.split(",")]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                post.tags.add(tag)
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
