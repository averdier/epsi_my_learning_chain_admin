# -*- coding: utf-8 -*-

from flask import request, g, current_app
from flask_restplus import Namespace, Resource, abort
from .. import auth
from ..serializers.sections import section_post_model, section_container, section_model
from app.models import Section, Campus

ns = Namespace('sections', description='Sections related operation')


# ================================================================================================
# ENDPOINTS
# ================================================================================================
#
#   API sections endpoints
#
# ================================================================================================

@ns.route('/')
class SectionCollection(Resource):
    decorators = [auth.login_required]

    @ns.marshal_with(section_container)
    def get(self):
        """
        Return Sections
        """
        # try:
        #    if 'campus' in dir(g.client):
        #        return {'sections': [s for s in Section.objects(campus=g.client.campus)]}
        # except Exception as ex:
        #    current_app.logger.debug('Error in introspection')
        #    current_app.logger.debug(ex)
        return {'sections': [s for s in Section.objects]}

    @ns.marshal_with(section_model)
    @ns.expect(section_post_model)
    def post(self):
        """
        Add Section
        """
        data = request.json
        c = Campus.objects.get_or_404(id=data['campus'])

        if Section.objects(name=data['name'], campus=c).count() > 0:
            abort(400, error='Name already exist')

        # Campus not needed in serializer
        # try:
        #     if 'campus' in dir(g.client):
        #         s = Section(
        #             campus=g.client.campus.id,
        #             year=data['year'],
        #             name=data['name']
        #         )
        #
        #         s.save()
        #
        #         return s
        # except Exception as ex:
        #     current_app.logger.debug('Error in introspection')
        #     current_app.logger.debug(ex)

        s = Section(
            campus=c,
            year=data['year'],
            name=data['name']
        )

        s.save()

        return s


@ns.route('/<id>')
@ns.response(404, 'Section not found')
class SectionItem(Resource):
    decorators = [auth.login_required]

    @ns.marshal_with(section_model)
    def get(self, id):
        """
        Return Section
        """
        s = Section.objects.get_or_404(id=id)

        # try:
        #    if 'campus' in dir(g.client):
        #        if g.client.campus.id != s.campus.id:
        #            abort(400, error='Not authorized')
        # except Exception as ex:
        #    current_app.logger.debug('Error in introspection')
        #    current_app.logger.debug(ex)

        return s

    @ns.response(204, 'Section successfully deleted')
    def delete(self, id):
        """
        Delete Section
        """
        s = Section.objects.get_or_404(id=id)

        # try:
        #    if 'campus' in dir(g.client):
        #        if g.client.campus.id != s.campus.id:
        #            abort(400, error='Not authorized')
        # except Exception as ex:
        #    current_app.logger.debug('Error in introspection')
        #    current_app.logger.debug(ex)

        s.delete()

        return 'Section successfully deleted', 204
