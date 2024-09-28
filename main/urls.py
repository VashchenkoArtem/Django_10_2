from .settings import main_app
import home
import tour

home.home_app.add_url_rule(
    rule = "/",
    view_func = home.render_home
)
tour.tour_app.add_url_rule(
    rule = "/tour/",
    view_func = tour.render_tour
)
main_app.register_blueprint(blueprint = home.home_app)
main_app.register_blueprint(blueprint = tour.tour_app)