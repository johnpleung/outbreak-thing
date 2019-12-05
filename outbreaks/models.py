from django.db import models
import datetime
import calendar
from django.utils.html import mark_safe
from markdown import markdown

# Field Choices

CONTAMINANT_CATEGORY_CHOICES = (
    ('PATHOGEN', 'Pathogen'),
    ('FOREIGN_SUBSTANCE', 'Foreign substance'),
    ('TOXIN', 'Toxin'),
    ('POTENTIAL_ALLERGEN', 'Potential allergen'),
    ('MULTIPLE', 'Multiple types'),
    ('OTHER', 'Other'),
)

US_STATE_CHOICES = (
    ('CA', 'CA'),
    ('TX', 'TX'),
    ('NV', 'NV'),
    ('NY', 'NY')
)

SEVERITY_CHOICES = (
    ('LOW', 'Low'),
    ('MEDIUM', 'Medium'),
    ('HIGH', 'High'),
    ('VARIES', 'Varies')
)

FOOD_TYPE_CHOICES = (
    ('DAIRY', 'Dairy'),
    ('FRUIT', 'Fruit'),
    ('GRAIN_BEAN_LEGUME', 'Grain/Bean/Legume'),
    ('MEAT', 'Meat'),
    ('CONFECTION', 'Confection'),
    ('VEGETABLE', 'Vegetable'),
    ('BEVERAGE', 'Beverage'),
    ('COOKING_OIL', 'Cooking oil'),
    ('SPICE', 'Spice'),
    ('CANNED_GOOD', 'Canned good'),
    ('ALCOHOL', 'Alcohol'),
    ('PREPARED_FOOD', 'Prepared food'),
    ('OTHER', 'Other'),
    ('MULTIPLE', 'Multiple types'),
)

class Contaminant(models.Model):
#    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=40, blank=True, null=True, choices=CONTAMINANT_CATEGORY_CHOICES)
    incident = models.ForeignKey('Incident', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'contaminants'

    def __str__(self):
        """String for representing this object."""
        return self.description

class Incident(models.Model):
    date_created = models.DateTimeField(blank=True, null=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    affected_food_description = models.CharField(max_length=255, blank=True, null=True)
    affected_food_type = models.CharField(max_length=40, blank=True, null=True, choices=FOOD_TYPE_CHOICES)
    severity = models.CharField(max_length=6, blank=True, null=True, choices=SEVERITY_CHOICES)
    details = models.TextField(max_length=8192, blank=True, null=True)

    class Meta:
        db_table = 'incidents'

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.details, safe_mode='escape'))

    def __str__(self):
        """String for representing this object."""
        return self.description

class Reference(models.Model):
    incident = models.ForeignKey('Incident', on_delete=models.CASCADE, null=True)
    org_name = models.CharField(max_length=40, blank=True, null=True)
    url = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        db_table = 'references'

    def __str__(self):
        """String for representing this object."""
        return self.org_name

class AffectedUSState(models.Model):
    incident = models.ForeignKey('Incident', related_name='affected_us_states', on_delete=models.CASCADE, null=True)
    abbrev = models.CharField(max_length=2, blank=True, null=True, choices=US_STATE_CHOICES)

    class Meta:
        db_table = 'affected_us_states'

    def __str__(self):
        """String for representing this object."""
        return self.abbrev