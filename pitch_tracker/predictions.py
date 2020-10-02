"""
This file is meant to be whatever model logic is needed for the Klio Pipeline.
Note this is for use as a tutorial and not productionization of a pipeline.
(There's probably more model caching that needs to happen)

"""

from crepe.core import process_file

# smaller models are faster to compute, but may yield less accurate pitch estimation
MODEL_CAPACITY_OPTIONS = ["tiny", "small", "medium", "large", "full"]


class MyModel:

    # Put any constants here needed for model prediction

    def __init__(self, model_capacity="small"):

        try:
            self.model_capacity = model_capacity
        except Exception as e:
            self.log.error('Model loading', e)
            raise e


    def predict(self, audio_input, output_directory):

        # Use default fields for viterbi, center, save_activation, save_plot, plot_voicing
        # step_size, verbose
        process_file(audio_input, output=output_directory, model_capacity=self.model_capacity)
