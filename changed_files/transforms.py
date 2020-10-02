"""
Notice: the code below is just an example of what can be done.

Feel free to import what's needed, including third-party libraries or
other self-written modules.
"""
import os
import tempfile

import apache_beam as beam
from apache_beam.io.gcp import gcsio

from klio.transforms import decorators
from pitch_tracker.predictions import MyModel

class HelloKlio(beam.DoFn):
    """A simple DoFn."""
    def setup(self):
        self.model = MyModel()

    @decorators.handle_klio
    def process(self, item):
        """Any errors raised here (explicitly or not), Klio will catch and
        log + drop the item.

        Args:
            item (KlioMessage): The current workitem, containing both
                the element reference, and the payload
        Returns:
            entity_id (str)
        """
        entity_id = item.element.decode("utf-8")
        job_config_data = self._klio.config.job_config.data
        input_location = job_config_data.inputs[0].location
        input_file = "{}/{}.wav".format(input_location, entity_id)
        output_dir = job_config_data.outputs[0].location

        print("input file: {}".format(input_file))
        self.model.predict(input_file, output_dir)
        yield item
