# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models


GRAPH_TYPES = (
    (0, 'Demand-Supply Graph'),
    (1, 'Labor Market'),
    (2, 'Labor Market (perfectly inelastic)'),
    (3, 'Cobb-Douglas'),
    (4, 'Labor Supply'),
    (5, 'Consumption - Saving'),
    (6, 'Saving - Investment'),
    (7, 'Money Market'),
)

INTERACTION_TYPES = (
    (0, 'Draggable lines'),
    (1, 'Area selection'),
)

COBB_DOUGLAS_SCENARIOS = (
    (0, 'Param 1 (A) increased'),
    (1, 'Param 1 (A) decreased'),
    (2, 'Param 2 (K) increased'),
    (3, 'Param 2 (K) decreased'),
    (4, 'Param 3 (α) increased'),
    (5, 'Param 3 (α) decreased'),
    (6, 'Param 4 (L) increased'),
    (7, 'Param 4 (L) decreased'),
)


class Graph(models.Model):
    class Meta:
        ordering = ('-created_at',)

    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    instructor_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    needs_submit = models.BooleanField(default=False)
    display_feedback = models.BooleanField(default=True)
    correct_feedback = models.TextField(blank=True, null=True)
    incorrect_feedback = models.TextField(blank=True, null=True)

    graph_type = models.PositiveSmallIntegerField(
        choices=GRAPH_TYPES,
        default=0)
    interaction_type = models.PositiveSmallIntegerField(
        choices=INTERACTION_TYPES,
        default=0)

    show_intersection = models.BooleanField(default=True)
    intersection_label = models.TextField(blank=True, null=True)
    intersection_label_editable = models.BooleanField(default=False)
    intersection_horiz_line_label = models.TextField(blank=True, null=True)
    intersection_horiz_line_label_editable = models.BooleanField(default=False)
    intersection_vert_line_label = models.TextField(blank=True, null=True)
    intersection_vert_line_label_editable = models.BooleanField(default=False)

    x_axis_label = models.TextField(blank=True, null=True)
    x_axis_label_editable = models.BooleanField(default=False)
    y_axis_label = models.TextField(blank=True, null=True)
    y_axis_label_editable = models.BooleanField(default=False)

    line_1_slope = models.DecimalField(max_digits=12, decimal_places=4)
    line_1_slope_editable = models.BooleanField(default=False)
    line_1_offset = models.DecimalField(
        max_digits=12, decimal_places=4, default=0)
    line_1_label = models.TextField(blank=True, null=True)
    line_1_label_editable = models.BooleanField(default=False)

    # The following are what the user is shown when line 1 is moved up
    # and down.
    line_1_feedback_increase = models.TextField(blank=True, null=True)
    line_1_increase_score = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    line_1_feedback_decrease = models.TextField(blank=True, null=True)
    line_1_decrease_score = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)

    line_2_slope = models.DecimalField(max_digits=12, decimal_places=4)
    line_2_slope_editable = models.BooleanField(default=False)
    line_2_offset = models.DecimalField(
        max_digits=12, decimal_places=4, default=0)
    line_2_label = models.TextField(blank=True, null=True)
    line_2_label_editable = models.BooleanField(default=False)

    # The following are what the user is shown when line 2 is moved up
    # and down.
    line_2_feedback_increase = models.TextField(blank=True, null=True)
    line_2_increase_score = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    line_2_feedback_decrease = models.TextField(blank=True, null=True)
    line_2_decrease_score = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)

    alpha = models.DecimalField(
        max_digits=12, decimal_places=4, default=Decimal('0.3'))

    # The following are input values for the Cobb-Douglas function,
    # only used if this is a Cobb-Douglas graph.
    cobb_douglas_a = models.DecimalField(
        max_digits=12, decimal_places=4, default=Decimal('2'),
        null=True, help_text='A = Total factor productivity')
    cobb_douglas_a_name = models.TextField(default='A')
    cobb_douglas_a_editable = models.BooleanField(default=False)
    cobb_douglas_l = models.DecimalField(
        max_digits=12, decimal_places=4, default=Decimal('0'),
        null=True, help_text='L = Labor input')
    cobb_douglas_l_name = models.TextField(default='L')
    cobb_douglas_l_editable = models.BooleanField(default=False)
    cobb_douglas_k = models.DecimalField(
        max_digits=12, decimal_places=4, default=Decimal('1'),
        null=True, help_text='K = Capital input')
    cobb_douglas_k_name = models.TextField(default='K')
    cobb_douglas_k_editable = models.BooleanField(default=False)
    cobb_douglas_alpha = models.DecimalField(
        max_digits=12, decimal_places=4, default=Decimal('0.65'),
        null=True, help_text='α = output elasticity of capital')
    cobb_douglas_alpha_name = models.TextField(default='α')
    cobb_douglas_alpha_editable = models.BooleanField(default=False)

    cobb_douglas_y_name = models.TextField(default='Y')

    cobb_douglas_correct_scenario = models.PositiveSmallIntegerField(
        choices=COBB_DOUGLAS_SCENARIOS,
        default=0,
        help_text='Define the correct scenario for this submittable graph.')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/graph/{}/'.format(self.pk)


class Submission(models.Model):
    class Meta:
        # A user can only have one submission per graph.
        unique_together = ('user', 'graph')

    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # The selection that the user made, encoded as a number.
    choice = models.PositiveSmallIntegerField(default=0)

    # Corresponds to the line_x_x_score
    score = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
