import flask

home_app = flask.Blueprint(
    name = "app",
    import_name = "home",
    template_folder = "templates"
)