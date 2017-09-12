# -*- coding: utf-8 -*-
import logging

from django import forms

from .fields import PhoneField

from ..bus.models import Route
from ..users.models import Grade, Phone

logger = logging.getLogger(__name__)


class PersonalInformationForm(forms.Form):

    def __init__(self, num_fields, *args, **kwargs):
        super(PersonalInformationForm, self).__init__(*args, **kwargs)

        self.num_emails = max(num_fields["emails"], 1)
        self.num_webpages = max(num_fields["websites"], 1)

        for i in range(self.num_emails):
            self.fields["email_{}".format(i)] = forms.EmailField(required=False, label="Email(s)")

        for i in range(self.num_webpages):
            self.fields["webpage_{}".format(i)] = forms.URLField(required=False, label="Webpage(s)")


class BusRouteForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(BusRouteForm, self).__init__(*args, **kwargs)
        self.BUS_ROUTE_CHOICES = [(None, "Set bus route...")]
        routes = Route.objects.all()
        for route in routes:
            self.BUS_ROUTE_CHOICES += [(route.route_name, route.route_name)]
        self.fields['bus_route'] = forms.ChoiceField(choices=self.BUS_ROUTE_CHOICES, widget=forms.Select)


class PreferredPictureForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        super(PreferredPictureForm, self).__init__(*args, **kwargs)
        self.PREFERRED_PICTURE_CHOICES = [("AUTO", "Auto-select the most recent photo")]

        photos = user.photo_permissions["self"]

        for i in range(4):
            grade = Grade.names[i]
            if photos[grade] is not None:
                self.PREFERRED_PICTURE_CHOICES += [(grade, grade.title() + " Photo")]

        self.fields["preferred_photo"] = forms.ChoiceField(choices=self.PREFERRED_PICTURE_CHOICES, widget=forms.RadioSelect(), required=True)


class PrivacyOptionsForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        super(PrivacyOptionsForm, self).__init__(*args, **kwargs)

        def flag(label, default):
            return forms.BooleanField(initial=default, label=label, required=False)

        self.fields["showaddress"] = flag(None, False)
        self.fields["showaddress-self"] = flag("Show Address", False)

        self.fields["showtelephone"] = flag(None, False)
        self.fields["showtelephone-self"] = flag("Show Phone", False)

        self.fields["showbirthday"] = flag(None, False)
        self.fields["showbirthday-self"] = flag("Show Birthday", False)

        pictures_label = "Show Pictures"
        if user.is_student:
            pictures_label += " on Import"
        self.fields["showpictures"] = flag(None, False)
        self.fields["showpictures-self"] = flag(pictures_label, False)

        photos = user.photo_permissions["self"]

        for i in range(4):
            grade = Grade.names[i]
            if photos[grade] is not None:
                self.fields["photoperm-{}".format(grade)] = flag(None, False)
                self.fields["photoperm-{}-self".format(grade)] = flag("Show {} Photo".format(grade.capitalize()), False)

        self.fields["showschedule"] = flag(None, False)
        self.fields["showschedule-self"] = flag("Show Class Schedule", False)

        self.fields["showeighth"] = flag(None, False)
        self.fields["showeighth-self"] = flag("Show Eighth Period Schedule", False)

        # self.fields["showlocker"] = flag(None, False)
        # self.fields["showlocker-self"] = flag("Show Locker", False)

        if not user.has_admin_permission("preferences"):
            for name in self.fields:
                if not name.endswith("-self"):
                    self.fields[name].widget.attrs['class'] = 'disabled'


class NotificationOptionsForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        super(NotificationOptionsForm, self).__init__(*args, **kwargs)

        def flag(label, default):
            return forms.BooleanField(initial=default, label=label, required=False)

        self.fields["receive_news_emails"] = flag("Receive News Emails", False)
        self.fields["receive_eighth_emails"] = flag("Receive Eighth Period Emails", False)


class PhoneForm(forms.ModelForm):

    """Represents a phone number (number + purpose)"""
    class Meta:
        model = Phone
        fields = ['purpose', 'number']
