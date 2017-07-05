"""Create views and route them to jinja2 files."""
from pyramid.view import view_config
from forbes.models import Billionaire


@view_config(route_name='billie_view', renderer='../templates/listing.jinja2')
def list_view(request):
    """View for the main listing page."""
    billie_entries = request.dbsession.query(Billionaire).all()
    return {"billie_entries": billie_entries}
