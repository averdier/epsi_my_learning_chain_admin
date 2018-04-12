# -*- coding: utf-8 -*-

from flask_restplus import fields
from .nested import group_nested
from .facilitators import facilitator_post_model, facilitator_patch_model
from .. import api


group_nested_with_project = api.inherit('Group nested with project ID', group_nested, {
    'project_id': fields.String(required=True, description='Project ID', attribute=lambda gr: gr.project.id)
})


student_post_model = api.model('Student POST model', {
    'first_name': fields.String(required=True, min_length=4, description='First name'),
    'last_name': fields.String(required=True, min_length=4, description='Last name'),
    'username': fields.String(required=True, min_length=6, description='Username'),
    'email': fields.String(required=True, description='Email address'),
    'secret': fields.String(required=True, min=6, description='Secret'),
    'img_uri': fields.String(required=False, description='Img uri'),
    'scopes': fields.List(fields.String(), required=True, description='Scopes'),
    'campus': fields.String(required=True, description='Campus ID'),
    'section': fields.String(required=True, description='Section ID')
})

student_patch_model = api.model('Student PATCH model', {
    'first_name': fields.String(required=False, min_length=4, description='First name'),
    'last_name': fields.String(required=False, min_length=4, description='Last name'),
    'email': fields.String(required=False, description='Email address'),
    'secret': fields.String(required=False, min=6, description='Secret'),
    'img_uri': fields.String(required=False, description='Img uri'),
    'scopes': fields.List(fields.String(), required=False, description='Scopes')
})

student_minimal_model = api.model('Student minimal model', {
    'id': fields.String(required=True, description='Student ID'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='First name'),
    'img_uri': fields.String(required=True, description='Img uri')
})

student_model = api.inherit('Student model', student_minimal_model, {
    'email': fields.String(required=True, description='Email'),
    'scopes': fields.List(fields.String(), required=True, description='Scopes'),
    'groups': fields.List(fields.Nested(group_nested_with_project), required=True, description='Groups list')
})

student_container = api.model('Student container', {
    'students': fields.List(fields.Nested(student_minimal_model), required=True, description='Students list')
})
