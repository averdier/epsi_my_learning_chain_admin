# -*- coding: utf-8 -*-

from runserver import app
from utils.iota import generate_seed

with app.test_request_context():
    from app.models import User, Campus, IOTAAddress

    IOTAAddress.objects()

    if Campus.objects(name='Arras').count() == 0:
        c = Campus(name='Arras', seed=generate_seed())
        c.save()

    else:
        c = Campus.objects(name='Arras').first()

    if User.objects(username='averdier').count() == 0:
        u = User(
            username='averdier',
            type='admin',
            scopes = [
                "canuser",
                "canproject",
                "cancreateproject",
                "canlistmyprojects",
                "canlistcampusprojects",
                "canviewproject",
                "cancreatecampus",
                "cancampus",
                "cancreateuser",
                "cancreatestudent",
                "cancreatefacilitator",
                "cansection",
                "cancreatesection",
                "canlistsection",
                "canreadsection",
                "canfacilitator",
                "canreadfacilitator",
                "canlistfacilitator",
                "cancampus",
                "cancreatecampus",
                "cangroup",
                "cancreategroup",
                "canclaim",
                "canlistclaim",
                "canlistfacilitator"
            ]
        )
        u.secret = 'averdier'
        u.save()

    print('db created.')
