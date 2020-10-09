"""
Notice: the code below is just an example of what can be done.

Feel free to import what's needed, including third-party libraries or
other self-written modules.
"""
import apache_beam as beam

from klio.transforms import decorators

from pitch_tracker.predictions import MyModel

class HelloKlio(beam.DoFn):
    """A simple DoFn."""
    def setup(self):
        self.model = MyModel()

    @decorators.handle_klio
    def process(self, data):
        element = data.element.decode("utf-8")
        self._klio.logger.info(
            "Received '%s' from file '%s'"
            % (element, self._klio.config.job_config.events.inputs[0].file_pattern)
        )

        job_config_data = self._klio.config.job_config.data 
        input_location = job_config_data.inputs[0].location
        input_file = "{}/{}.wav".format(input_location, element)
        output_dir = job_config_data.outputs[0].location        
        self.model.predict(input_file, output_dir)
        yield data
