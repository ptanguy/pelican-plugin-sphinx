from pelican import signals
from pelican.generators import CachingGenerator


class SphinxDocsGenerator(CachingGenerator):
    """Generate html pages with current pelican template
    of from sphinx .rst files"""

    def __init__(self, *args, **kwargs):
        super(SphinxDocsGenerator, self).__init__(*args, **kwargs)
        if 'SPHINX_DOC_SRC' in self.settings:
            self.sphinx_doc_src = self.settings['SPHINX_DOC_SRC']

    def generate_context(self):
        #TODO use sphinx websupport
        #signals.page_generator_finalized.send(self)
        pass

    def generate_output(self, writer):
        pass
        #signals.page_writer_finalized.send(self, writer=writer)

def register():
    signals.get_generators.connect(SphinxDocsGenerator)
