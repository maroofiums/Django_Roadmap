from crispy_forms.layout import LayoutObject, TEMPLATE_PACK, Div, Submit
from django.template.loader import render_to_string

class FormField(LayoutObject):
    template = "crispy_components/form_field.html"

    def __init__(self, field_name, placeholder="", css_class=""):
        self.field_name = field_name
        self.placeholder = placeholder
        self.css_class = css_class

    # FIX: include **context parameter** and default template_pack
    def render(self, form, form_style, context=None, template_pack=TEMPLATE_PACK):
        if context is None:
            context = {}
        context.update({
            "field_name": self.field_name,
            "placeholder": self.placeholder,
            "css_class": self.css_class,
            "form": form,
        })
        return render_to_string(self.template, context)


def CardLayout(*fields):
    return Div(*fields, css_class="card p-4 shadow")

def PrimarySubmit(label="Submit"):
    return Submit("submit", label, css_class="btn btn-primary w-100 mt-3")
