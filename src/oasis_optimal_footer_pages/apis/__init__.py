from nomad.config.models.plugins import APIEntryPoint


class MyAPIEntryPoint(APIEntryPoint):
    def load(self):
        from oasis_optimal_footer_pages.apis.footer_pages import app

        return app


oasis_optimal_footer_pages = MyAPIEntryPoint(
    prefix='oasis_optimal_footer_pages',
    name='oasis_optimal_footer_pages',
    description='OPTIMAL Oasis footer pages.',
)
