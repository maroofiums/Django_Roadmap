# 📅 **Week 9 – Crispy Forms & Advanced Forms (6 Days + 1 Revision Day)**

---

# ✅ **Day 1 — Install Crispy Forms + Basic Integration**

### 🎯 Targets

• django-crispy-forms install
• Bootstrap template integrate
• Existing signup/login forms ko crispy bana dena

### 🛠️ Steps

1. Install

```
pip install django-crispy-forms crispy-bootstrap5
```

2. **settings.py**

```python
INSTALLED_APPS = [
    ...
    'crispy_forms',
    'crispy_bootstrap5',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

3. Template mein load:

```html
{% load crispy_forms_tags %}
{{ form|crispy }}
```

### 📝 Outcome

Login + Signup forms atra-tatra nahi lagenge. Proper spacing, alignment, labels — sab auto responsive.

---

# ✅ **Day 2 — FormHelper + Custom Layouts**

(Most important day)

### 🎯 Targets

• FormHelper use karna
• Custom layout, field ordering
• Submit buttons add karna, Div(), Row(), Column()

### 🛠️ Example (`forms.py`)

```python
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django import forms

class ProfileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    bio = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('first_name'),
                Column('last_name'),
            ),
            'bio',
            Submit('submit', 'Save Profile')
        )
```

### 📝 Outcome

Forms will look intentional — 2-column layout, smart spacing, neat alignment.

---

# ✅ **Day 3 — Advanced Layouts + Custom Templates**

### 🎯 Targets

• Card-style form layouts
• Buttons center align
• Floating labels (Bootstrap utility)

### 🛠️ Steps

You will create **beautiful card-styled forms** for Post Create/Update.

Example:

```python
self.helper.layout = Layout(
    Div(
        Row(
            Column('title', css_class='form-floating mb-3'),
        ),
        Row(
            Column('content', css_class='form-floating mb-3'),
        ),
        Submit('submit', 'Save', css_class='btn btn-primary w-100'),
        css_class='card p-4 shadow'
    )
)
```

### 📝 Outcome

Your Blog app feels like a real professional dashboard.

---

# ✅ **Day 4 — Reusable Form Components**

### 🎯 Targets

• Make components that multiple forms can reuse
• Example: Custom input component
• Custom submit button component

### 🛠️ Steps

Create `templates/components/` folder:

`components/submit_button.html`

```html
<button type="submit" class="btn btn-success w-100">{{ text }}</button>
```

Then call:

```python
from crispy_forms.layout import HTML

self.helper.layout = Layout(
    'title',
    'content',
    HTML("{% include 'components/submit_button.html' with text='Save Post' %}")
)
```

### 📝 Outcome

Future forms become 5× faster to write.

---

# ✅ **Day 5 — Custom Validation + Error Messages + Clean Methods**

### 🎯 Targets

• Custom validators
• `clean()` method
• Custom error messages crispy style

Example:

```python
def clean_title(self):
    t = self.cleaned_data['title']
    if "bad" in t.lower():
        raise forms.ValidationError("Avoid using banned words.")
    return t
```

### 📝 Outcome

Your forms become smart — they guide users instead of silently failing.

---

# ✅ **Day 6 — Project Day: Convert Full Blog App Forms**

### 🎯 Targets

• Signup Form with crispy
• Login Form crispy
• CreatePostForm crispy
• UpdatePostForm crispy
• Delete confirmation stylish

All forms should be:

* With card layout
* 2-column fields where needed
* Custom buttons
* Nice spacing
* Clean validation

Ye day tumhari full polish day hogi.

---

# 🧠 **Day 7 — Revision + Small Quiz + Cleanup**

### Activities

* Revise FormHelper
* Check layouts ka working
* Organize templates
* Tiny quiz on your concepts
* Fix any bugs

---

# ⭐ If you want, I can also:

* Create full boilerplate code for every day
* Add screenshots-style UI using Bootstrap
* Make your Blog app feel like a **real modern CMS**
